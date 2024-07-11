from dataclasses import dataclass
from typing import Optional

from requests import Response
from returns.result import Result, Success, Failure

from client.api_requests.api.NotionAPIDatabasesClient import NotionAPIDatabasesClient
from client.api_requests.custom_types import json_
from client.api_requests.errors.CustomError import CustomError
from database.DatabaseDTO import DatabaseDTO


@dataclass
class NotionDatabaseProvider:
    notion_client: NotionAPIDatabasesClient

    def create_database(self, data: DatabaseDTO) -> Result[CustomError, DatabaseDTO]:
        return self.notion_client.create_database(data.json())

    def query_database(self, database_id: str, data: json_, query_params: Optional[str] = None) -> Response:
        return self.notion_client.query_database(database_id, data, query_params)

    def retrieve_database(self, database_id: str) -> Result[CustomError, DatabaseDTO]:
        response = self.notion_client.retrieve_database(database_id)
        if response.status_code == 200:
            return Success(DatabaseDTO(**response.json()))
        return Failure(CustomError(response.status_code, response.text))

    def update_database(self, database_id: str, data: json_) -> Response:
        return self.notion_client.update_database(database_id, data)
