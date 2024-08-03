from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from requests import Response
from returns.result import Result, Success, Failure

from Block import Block
from BlockTypeFactory import create_concrete_block_type
from CustomError import CustomError
from client.api_requests.api.NotionAPIBlocksClient import NotionAPIBlocksClient
from custom_types import json_
from status_codes import SUCCESS, ERROR


def _access_children(response: Response) -> Optional[json_]:
    return response.json()['results']


def _access_child_id(child: json_) -> str:
    return child['id']


def _create_children_block_data(children_blocks: list[Block], after_block_id: str) -> json_:
    children = dict()
    children['children'] = [child.model_dump(
        mode='json', exclude_none=True, exclude={
            'id', 'parent', 'archived', 'in_trash'}) for child in children_blocks]
    if after_block_id:
        children['after'] = after_block_id
    return children


def _parse_result(response: json_) -> list[Block]:
    results = response['results']
    return [create_concrete_block_type(block) for block in results]


@dataclass
class NotionBlockProvider:
    """
    A client to interact with the Notion API Blocks part programmatically using a custom DSL - object blocks and
    its children specific subtypes.

    Attributes:
        notion_client (NotionAPIBlocksClient): The helper class object to pass along the requests to the Notion API.

    Methods:
        create_block(block: Block) -> Result[CustomError, bool]:
            Creates a block in the Notion API with the values of the passed in block parameter.
        append_block_children(block_id: str, children_blocks: list[Block], after_block_id: str = '') -> Result[CustomError, bool]:
            Appends children blocks to an existing block in the Notion API.
        set_block_children(block: Block) -> Result[CustomError, bool]:
            Sets the block parameter object children in the Notion API to the block objects in the children attribute.
        retrieve_block(block_id: str, retrieve_children: bool = True) -> Result[CustomError, Block]:
            Retrieve a block from the Notion API. By default, retrieves children blocks recursively.
        retrieve_block_children(block: Block, recursively: bool = True) -> Result[CustomError, Block]:
            Recursively retrieves and appends children blocks to a given block.
        update_block(block: Block) -> Result[CustomError, bool]:
            Updates a block in the Notion API with the values of the passed in block parameter.
        delete_block_with_id(block_id: str) -> Result[CustomError, bool]:
            Deletes a block from the Notion API using its ID.
        delete_block(block: Block) -> Result[CustomError, bool]:
            Deletes a block from the Notion API using a Block object.
    """
    notion_client: NotionAPIBlocksClient

    def create_block(self, block: Block) -> Result[CustomError, Block]:
        """
        Creates a block in the Notion API with the values of the passed in block parameter.

        Parameters:
            block (Block): The block to create. It will be created based on the values of the attributes of this
            block. ID, archived and in_trash attributes will be ignored, as they are redundant as the block has not
            even been created yet. The block will be attached to the parent specified in the parent attribute at the
            end of its list of children.

        Returns:
            Result[CustomError, bool]: True if the creation is successful,
                                       or a Failure containing a CustomError if the creation fails.
        """
        result = self.append_block_children(block.parent.get_parent_id(), [block])
        if isinstance(result, Failure):
            return Failure(result.failure())
        return Success(result.unwrap()[0])

    def append_block_children(self, block_id: str, children_blocks: list[Block], after_block_id: str = '') -> \
            Result[CustomError, list[Block]]:
        """
        Appends children blocks to an existing block in the Notion API. By default, appends the children at the end
        of the children blocks list or after the id of the block specified in the after_block_id parameter. The id of
        the block objects in the children are ignored, as these are new block objects that will be created. So this
        functionality is used to create blocks.

        From Notion Documentation:
        Existing blocks cannot be moved using this endpoint. Blocks are appended to the bottom of the parent block.
        To append a block in a specific place other than the bottom of the parent block, use the "after"(
        after_block_id) parameter and  set its value to the ID of the block that the new block should be appended after.
        Once a block is appended as a child, it can't be moved elsewhere via the API.

        Parameters:
            block_id (str): The id of the block to which children will be appended.
            children_blocks (list, Block): The list of children blocks to append.
            after_block_id (str): The ID of the block after which the children will be appended.
                                            If not provided, then by default, the children will be appended at the
                                            end of the parent block as that is the default behavior in Notion.

        Returns:
            Result[CustomError, bool]: True if the operation is successful,
                                       or a Failure containing a CustomError if the operation fails.
        """
        children = _create_children_block_data(children_blocks, after_block_id)
        response = self.notion_client.append_block_children(block_id, children)
        if response.status_code != SUCCESS:
            return Failure(CustomError(message=response.text, status_code=response.status_code))
        try:
            return Success(_parse_result(response.json()))
        except Exception as e:
            return Failure(CustomError(message=str(e), status_code=ERROR))

    def set_block_children(self, block: Block) -> Result[CustomError, list[Block]]:
        """
        Sets the block parameter object children in the Notion API to the block objects in the children attribute.
        The ordering will be set based on the order of the children attribute list. Any children which are currently
        attached in notion to the block and are not present in the list will be deleted.

        Parameters:
            block (Block): The block whose children are to be set in the Notion API.

        Returns:
            Result[CustomError, bool]: True if the operation is successful,
                                       or a Failure containing a CustomError if the operation fails.
        """
        notion_block = self.retrieve_block(block.id.hex)
        if isinstance(notion_block, Failure):
            return Failure(notion_block.failure())

        for child in notion_block.unwrap().children:
            result = self.delete_block(child)
            if isinstance(result, Failure):
                return Failure(result.failure())

        return self.append_block_children(block.id.hex, block.children)

    def retrieve_block(self, block_id: str, retrieve_children: bool = True) -> Result[CustomError, Block]:
        """
        Retrieve a block from the Notion API. By default, automatically retrieves and adds the children blocks
        recursively to the children parameter of the resulting Block.

        Parameters:
            block_id (str): The ID of the block to retrieve.
            retrieve_children (bool): Whether to retrieve and add the children block to the resulting Block. If set to False the children attribute will contain an empty list

        Returns:
            Result[CustomError, Block]: A Success containing the retrieved Block if the operation is successful,
                                        or a Failure containing a CustomError if the operation fails.
        """
        response = self.notion_client.retrieve_block(block_id)
        if response.status_code != SUCCESS:
            return Failure(CustomError(response.status_code, response.text))

        try:
            block = create_concrete_block_type(response.json())
        except Exception as e:
            return Failure(CustomError(message=str(e), status_code=ERROR))

        if block.has_children and retrieve_children:
            result = self.retrieve_block_children(block)
            if isinstance(result, Failure):
                return result

        return Success(block)

    def retrieve_block_children(self, block: Block, recursively: bool = True) -> Result[CustomError, Block]:
        """
         Retrieves and appends children blocks to a given block to his children attribute. Any objects in the children
         attribute of the block parameter will be overwritten and removed. By default, it is set to
         recursively retrieve the children of the children blocks as well.

         Parameters:
             block (Block): The parent block whose children are to be retrieved.
             recursively (bool): Whether to retrieve the children of the children blocks as well, by default True

         Returns:
             Result[CustomError, Block]: A Success containing the block with its children if the operation is successful,
                                         or a Failure containing a CustomError if the operation fails.
         """
        block.children = []
        result = self.retrieve_children(block.id, recursively)
        if isinstance(result, Failure):
            return Failure(result.failure())
        block.children = result.unwrap()
        return Success(block)

    def retrieve_children(self, _id: UUID, recursively: bool = True) -> Result[CustomError, list[Block]]:
        result_children = []
        response = self.notion_client.retrieve_block_children(_id.hex)
        if response.status_code != SUCCESS:
            return Failure(CustomError(response.status_code, response.text))

        try:
            children = _access_children(response)
        except Exception as e:
            return Failure(CustomError(message=str(e), status_code=ERROR))
        for block_child in children:
            child = self.retrieve_block(_access_child_id(block_child), recursively)
            if isinstance(child, Failure):
                return Failure(child.failure())
            result_children.append(child.unwrap())

        return Success(result_children)

    def update_block(self, block: Block) -> Result[CustomError, Block]:
        """
         Updates a block in the Notion API with the values of the passed in block parameter. The id of the block will be
         taken from the Block parameter

         Parameters:
             block (Block): The block to update. It will be updated based on the values of the parameters of this block.

         Returns:
             Result[CustomError, bool]: True if the update is successful,
                                        or a Failure containing a CustomError if the update fails.
         """
        data = block.model_dump(mode='json', exclude_none=True)
        response = self.notion_client.update_block(block.id.hex, data)
        if response.status_code != SUCCESS:
            return Failure(CustomError(response.status_code, response.text))

        try:
            return Success(create_concrete_block_type(response.json()))
        except Exception as e:
            return Failure(CustomError(message=str(e), status_code=ERROR))

    def delete_block_with_id(self, block_id: str) -> Result[CustomError, bool]:
        """
         Deletes a block from the Notion API with the specified ID.

         Parameters:
             block_id (str): The ID of the block to delete.

         Returns:
             Result[CustomError, bool]: True if the deletion is successful,
                                        or a Failure containing a CustomError if the deletion fails.
         """
        response = self.notion_client.delete_block(block_id)
        return True if response.status_code == SUCCESS else Failure(CustomError(response.status_code, response.text))

    def delete_block(self, block: Block) -> Result[CustomError, bool]:
        """
        Deletes a block from the Notion API with the specified ID container in the Block object.

        Parameters:
            block (Block): The block to delete.

        Returns:
            Result[CustomError, bool]: True if the deletion is successful,
                                       or a Failure containing a CustomError if the deletion fails.
        """
        return self.delete_block_with_id(block.id.hex)
