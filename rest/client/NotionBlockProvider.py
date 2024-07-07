from dataclasses import dataclass
from typing import Optional

from block.BlockDTO import BlockDTO
from client.requests.api.NotionAPIClient import NotionAPIClient


@dataclass
class NotionBlockProvider:
    notion_client: NotionAPIClient

    def get_block(self, block_id: str) -> Optional[BlockDTO]:
        response = self.notion_client.get_database(block_id)
        return None if response is None else BlockDTO(**response)
