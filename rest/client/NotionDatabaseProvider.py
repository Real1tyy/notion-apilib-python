from typing import Optional

from client.NotionAPIClient import NotionAPIClient
from database.DatabaseDTO import DatabaseDTO


class NotionDatabaseProvider:

    def __init__(self, notion_api_client: NotionAPIClient):
        self.notion_client = notion_api_client

    def get_database(self, database_id: str) -> Optional[DatabaseDTO]:
        response = self.notion_client.get_database(database_id)
        return None if response is None else DatabaseDTO(**response)
