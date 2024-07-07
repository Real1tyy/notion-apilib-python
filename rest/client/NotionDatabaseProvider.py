from dataclasses import dataclass
from typing import Optional

from requests import Response

from client.requests.api.NotionAPIDatabasesClient import NotionAPIDatabasesClient
from client.requests.types import json_


@dataclass
class NotionDatabaseProvider:
    notion_client: NotionAPIDatabasesClient

    def create_database(self, data: json_) -> Response:
        return self.notion_client.create_database(data)

    def query_database(self, database_id: str, data: json_, query_params: Optional[str] = None) -> Response:
        return self.notion_client.query_database(database_id, data, query_params)

    def retrieve_database(self, database_id: str) -> Response:
        return self.notion_client.retrieve_database(database_id)

    def update_database(self, database_id: str, data: json_) -> Response:
        return self.notion_client.update_database(database_id, data)
