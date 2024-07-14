from dataclasses import dataclass
from typing import Optional

from returns.result import Result, Success, Failure

from BlockDTO import BlockDTO
from CustomError import CustomError
from client.api_requests.api.NotionAPIBlocksClient import NotionAPIBlocksClient
from client.api_requests.custom_types import json_


@dataclass
class NotionBlockProvider:
    notion_client: NotionAPIBlocksClient

    def append_block_children(self, block_id: str, data: json_) -> Optional[json_]:
        response = self.notion_client.append_block_children(block_id, data)

    def retrieve_block(self, block_id: str) -> Result[CustomError, BlockDTO]:
        response = self.notion_client.retrieve_block(block_id)
        # print(response.json())
        if response.status_code == 200:
            return Success(BlockDTO(**response.json()))
        return Failure(CustomError(response.status_code, response.text))

    def retrieve_block_children(self, block_id: str, query_params: Optional[str] = None) -> Optional[json_]:
        response = self.notion_client.retrieve_block_children(block_id, query_params)
        return response.json()

    def update_block(self, block_id: str, data: json_) -> Optional[json_]:
        response = self.notion_client.update_block(block_id, data)

    def delete_block(self, block_id: str) -> bool:
        response = self.notion_client.delete_block(block_id)
        return True if response.status_code == 200 else False
