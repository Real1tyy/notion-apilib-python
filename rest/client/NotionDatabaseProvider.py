from dataclasses import dataclass
from typing import Optional

from client.requests.api.NotionAPIClient import NotionAPIClient
from database.DatabaseDTO import DatabaseDTO


@dataclass
class NotionDatabaseProvider:
    notion_client: NotionAPIClient

    def get_database(self, database_id: str) -> Optional[DatabaseDTO]:
        response = self.notion_client.notion_databases_client.retrieve_database(database_id)
        return None if response is None else DatabaseDTO(**response)

    def query_database(self, database_id: str) -> Optional[DatabaseDTO]:
        response = self.notion_client.notion_databases_client.query_database(database_id)
        return None if response is None else DatabaseDTO(**response)
