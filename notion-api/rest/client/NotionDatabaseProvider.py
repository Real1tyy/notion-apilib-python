from dataclasses import dataclass
from typing import Optional

from requests import Response
from returns.result import Result, Success, Failure

from Database import Database, create_database
from Page import create_page
from client.api_requests.api.NotionAPIDatabasesClient import NotionAPIDatabasesClient
from client.api_requests.errors.CustomError import CustomError
from custom_types import json_
from status_codes import SUCCESS, ERROR
from utils import _access_children


@dataclass
class NotionDatabaseProvider:
    notion_client: NotionAPIDatabasesClient

    def create_database(self, database: Database) -> Result[CustomError, Database]:
        data = database.deserialize_json()
        response = self.notion_client.create_database(data)
        if response.status_code != SUCCESS:
            return Failure(CustomError(message=response.text, status_code=response.status_code))

        try:
            database = create_database(response.json())
            return Success(database)
        except Exception as e:
            return Failure(CustomError(message=str(e), status_code=ERROR))

    def query_database(self, database: Database, query_params: Optional[str] = None) -> Response:
        response = self.notion_client.query_database(database.id.hex, {}, query_params)

        if response.status_code != SUCCESS:
            return Failure(CustomError(response.status_code, response.text))

        _json = response.json()
        has_more = _json['has_more']
        next_cursor = _json['next_cursor']
        try:
            children = _access_children(response)
        except Exception as e:
            return Failure(CustomError(message=str(e), status_code=ERROR))

        for page_json in children:
            page = create_page(page_json)
            database.pages.append(page)

        return self.query_paginated_database(database, next_cursor=next_cursor)

    def query_paginated_database(self, database: Database, next_cursor: str):
        data = {'start_cursor': next_cursor}
        response = self.notion_client.query_database(database.id.hex, data, None)

        dataa = response.json()
        has_more = dataa['has_more']
        next_cursor = dataa['next_cursor']

        try:
            children = _access_children(response)
        except Exception as e:
            return Failure(CustomError(message=str(e), status_code=ERROR))

        for page_json in children:
            try:
                page = create_page(page_json)
            except Exception as e:
                print(page_json['properties'])
                raise e
            database.pages.append(page)
        if has_more:
            self.query_paginated_database(database, next_cursor=next_cursor)

        return database

    def retrieve_database(self, database_id: str) -> Result[CustomError, Database]:
        response = self.notion_client.retrieve_database(database_id)
        if response.status_code != SUCCESS:
            return Failure(CustomError(response.status_code, response.text))
        database = create_database(response.json())

        return Success(database)

    def update_database(self, database_id: str, data: json_) -> Response:
        return self.notion_client.update_database(database_id, data)

# how to retrieve the latest results from a Notion database
# {
#  "timestamp": "last_edited_time",
#  "direction": "descending"
# }
