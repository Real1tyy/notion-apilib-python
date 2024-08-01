from dataclasses import dataclass
from typing import Optional

from requests import Response
from returns.result import Result, Success, Failure

from Database import Database
from client.api_requests.api.NotionAPIDatabasesClient import NotionAPIDatabasesClient
from client.api_requests.errors.CustomError import CustomError
from custom_types import json_


@dataclass
class NotionDatabaseProvider:
    notion_client: NotionAPIDatabasesClient

    def create_database(self, data: Database) -> Result[CustomError, Database]:
        response = self.notion_client.create_database(data.model_dump(mode='json'))
        if response.status_code == 200:
            return Success(Database(**response.json()))
        return Failure(CustomError(response.status_code, response.text))

    def query_database(self, database_id: str, data: json_, query_params: Optional[str] = None) -> Response:
        return self.notion_client.query_database(database_id, data, query_params)

    def retrieve_database(self, database_id: str) -> Result[CustomError, Database]:
        response = self.notion_client.retrieve_database(database_id)
        if response.status_code == 200:
            return Success(Database(**response.json()))
        return Failure(CustomError(response.status_code, response.text))

    def update_database(self, database_id: str, data: json_) -> Response:
        return self.notion_client.update_database(database_id, data)
