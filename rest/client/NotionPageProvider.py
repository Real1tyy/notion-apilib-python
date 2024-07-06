from typing import Optional

from client.NotionAPIClient import NotionAPIClient
from page.PageDTO import PageDTO


class NotionPagesProvider:

    def __init__(self, notion_api_client: NotionAPIClient):
        self.notion_client = notion_api_client

    def get_page(self, page_id: str) -> Optional[PageDTO]:
        response = self.notion_client.get_database(page_id)
        return None if response is None else PageDTO(**response)
