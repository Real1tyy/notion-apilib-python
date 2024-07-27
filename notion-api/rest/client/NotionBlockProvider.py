from dataclasses import dataclass
from typing import Optional

from returns.result import Result, Success, Failure

from Block import Block
from CustomError import CustomError
from block_types.BlockTypeFactory import BlockTypeFactory
from client.api_requests.api.NotionAPIBlocksClient import NotionAPIBlocksClient
from client.api_requests.custom_types import json_


@dataclass
class NotionBlockProvider:
    notion_client: NotionAPIBlocksClient

    def append_block_children(self, block_id: str, data: json_) -> Optional[json_]:
        response = self.notion_client.append_block_children(block_id, data)

    def retrieve_block(self, block_id: str) -> Result[CustomError, Block]:
        response = self.notion_client.retrieve_block(block_id)
        if response.status_code == 200:
            block = BlockTypeFactory.create_concrete_type_dto(response.json())
            if block.has_children:
                return self.retrieve_block_children(block)
            return Success(block)
        return Failure(CustomError(response.status_code, response.text))

    def retrieve_block_children(self, block: Block) -> Result[CustomError, Block]:
        response = self.notion_client.retrieve_block_children(block.id.hex)
        for block_child in response.json()['results']:
            child = self.retrieve_block(block_child['id'])
            if isinstance(child, Success):
                block.children.append(child.unwrap())
            else:
                return child

        return Success(block)

    def update_block(self, block_id: str, data: json_) -> Optional[json_]:
        response = self.notion_client.update_block(block_id, data)

    def delete_block(self, block_id: str) -> bool:
        response = self.notion_client.delete_block(block_id)
        return True if response.status_code == 200 else False
