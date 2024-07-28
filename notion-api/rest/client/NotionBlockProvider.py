from dataclasses import dataclass
from typing import Optional

from requests import Response
from returns.result import Result, Success, Failure

from Block import Block
from CustomError import CustomError
from block_types.BlockTypeFactory import BlockTypeFactory
from client.api_requests.api.NotionAPIBlocksClient import NotionAPIBlocksClient
from client.api_requests.custom_types import json_


def access_children(response: Response) -> Optional[json_]:
    return response.json()['results']


def access_child_id(child: json_) -> str:
    return child['id']


@dataclass
class NotionBlockProvider:
    notion_client: NotionAPIBlocksClient

    def append_block_children(self, block_id: str, data: json_) -> Result[CustomError, bool]:
        response = self.notion_client.append_block_children(block_id, data)

    def retrieve_block(self, block_id: str) -> Result[CustomError, Block]:
        response = self.notion_client.retrieve_block(block_id)
        if response.status_code == 200:
            block = BlockTypeFactory.create_concrete_type_dto(response.json())
            if block.has_children:
                result = self._retrieve_block_children(block)
                if isinstance(result, Failure):
                    return result

            return Success(block)
        return Failure(CustomError(response.status_code, response.text))

    def _retrieve_block_children(self, block: Block) -> Result[CustomError, Block]:
        response = self.notion_client.retrieve_block_children(block.id.hex)
        if response.status_code != 200:
            return Failure(CustomError(response.status_code, response.text))

        children = access_children(response)
        for block_child in children:
            child = self.retrieve_block(access_child_id(block_child))
            if isinstance(child, Success):
                block.children.append(child.unwrap())
            else:
                return child

        return Success(block)

    def update_block(self, block: Block) -> Result[CustomError, bool]:
        data = block.model_dump(mode='json', exclude_none=True)
        response = self.notion_client.update_block(block.id.hex, data)
        return True if response.status_code == 200 else Failure(CustomError(response.status_code, response.text))

    def delete_block_with_id(self, block_id: str) -> Result[CustomError, bool]:
        response = self.notion_client.delete_block(block_id)
        return True if response.status_code == 200 else Failure(CustomError(response.status_code, response.text))

    def delete_block(self, block: Block) -> Result[CustomError, bool]:
        return self.delete_block_with_id(block.id.hex)
