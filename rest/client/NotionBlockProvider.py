from typing import Optional

from block.BlockDTO import BlockDTO
from client.NotionAPIClient import NotionAPIClient


class NotionBlockProvider:

    def __init__(self, notion_api_client: NotionAPIClient):
        self.notion_client = notion_api_client

    def get_block(self, block_id: str) -> Optional[BlockDTO]:
        response = self.notion_client.get_database(block_id)
        return None if response is None else BlockDTO(**response)
