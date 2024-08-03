import json
from dataclasses import dataclass
from typing import Optional

from requests import Response
from returns.result import Result, Success, Failure

from Database import Database, create_database
from client.api_requests.api.NotionAPIDatabasesClient import NotionAPIDatabasesClient
from client.api_requests.errors.CustomError import CustomError
from custom_types import json_
from status_codes import SUCCESS, ERROR


@dataclass
class NotionDatabaseProvider:
    notion_client: NotionAPIDatabasesClient

    def create_database(self, database: Database) -> Result[CustomError, Database]:
        data = database.deserialize_json()
        print(json.dumps(data, indent=4))
        response = self.notion_client.create_database(data)
        if response.status_code != SUCCESS:
            return Failure(CustomError(message=response.text, status_code=response.status_code))
        try:
            database = create_database(response.json())
            return Success(database)
        except Exception as e:
            return Failure(CustomError(message=str(e), status_code=ERROR))

    def query_database(self, database_id: str, data: json_, query_params: Optional[str] = None) -> Response:
        return self.notion_client.query_database(database_id, data, query_params)

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
