from dataclasses import dataclass
from typing import Optional

from client.api_requests.api.NotionAPIBlocksClient import NotionAPIBlocksClient
from client.api_requests.custom_types import json_


@dataclass
class NotionBlockProvider:
    notion_client: NotionAPIBlocksClient

    def append_block_children(self, block_id: str, data: json_) -> Optional[json_]:
        response = self.notion_client.append_block_children(block_id, data)

    def retrieve_block(self, block_id: str) -> Optional[json_]:
        response = self.notion_client.retrieve_block(block_id)

    def retrieve_block_children(self, block_id: str, query_params: Optional[str] = None) -> Optional[json_]:
        response = self.notion_client.retrieve_block_children(block_id, query_params)

    def update_block(self, block_id: str, data: json_) -> Optional[json_]:
        response = self.notion_client.update_block(block_id, data)

    def delete_block(self, block_id: str) -> bool:
        response = self.notion_client.delete_block(block_id)
        return True if response.status_code == 200 else False
