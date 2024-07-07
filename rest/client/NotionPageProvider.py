from dataclasses import dataclass
from typing import Optional

from client.requests.api.NotionAPIClient import NotionAPIClient
from page.PageDTO import PageDTO


@dataclass
class NotionPageProvider:
    notion_client: NotionAPIClient

    def get_page(self, page_id: str) -> Optional[PageDTO]:
        response = self.notion_client.get_database(page_id)
        return None if response is None else PageDTO(**response)
