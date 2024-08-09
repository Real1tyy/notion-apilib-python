# Standard Library
from dataclasses import dataclass
from uuid import UUID

from returns.result import Failure, Result

# Third Party
from ApiError import ApiError
from block import Block
from client.api_requests.api.NotionAPIBlocksClient import NotionAPIBlocksClient
from custom_types import json_
from decorators import handle_exceptions
from status_codes import SUCCESS
from type_factory import deserialize_block
from utils import _access_child_id, _access_children


def _create_children_block_data(children_blocks: list[Block], after_block_id: str) -> json_:
    children = dict()
    children['children'] = [child.serialize_to_json() for child in children_blocks]
    if after_block_id:
        children['after'] = after_block_id
    return children


def _parse_result(response: json_) -> list[Block]:
    results = response['results']
    return [deserialize_block(block) for block in results]


@dataclass
class NotionBlockProvider:
    """
    A client to interact with the Notion API Blocks part programmatically using a custom DSL - object _blocks and
    its children specific subtypes.

    Attributes:
        notion_client (NotionAPIBlocksClient): The helper class object to pass along the requests to the Notion API.

    Methods:
        create_block(_blocks: Block) -> Result[CustomError, bool]:
            Creates a _blocks in the Notion API with the values of the passed in _blocks parameter.
        append_block_children(block_id: str, children_blocks: list[Block], after_block_id: str = '') -> Result[CustomError, bool]:
            Appends children _blocks to an existing _blocks in the Notion API.
        set_block_children(_blocks: Block) -> Result[CustomError, bool]:
            Sets the _blocks parameter object children in the Notion API to the _blocks objects in the children attribute.
        retrieve_block(block_id: str, retrieve_children: bool = True) -> Result[CustomError, Block]:
            Retrieve a _blocks from the Notion API. By default, retrieves children _blocks recursively.
        retrieve_block_children(_blocks: Block, recursively: bool = True) -> Result[CustomError, Block]:
            Recursively retrieves and appends children _blocks to a given _blocks.
        update_block(_blocks: Block) -> Result[CustomError, bool]:
            Updates a _blocks in the Notion API with the values of the passed in _blocks parameter.
        delete_block_with_id(block_id: str) -> Result[CustomError, bool]:
            Deletes a _blocks from the Notion API using its ID.
        delete_block(_blocks: Block) -> Result[CustomError, bool]:
            Deletes a _blocks from the Notion API using a Block object.
    """
    notion_client: NotionAPIBlocksClient

    @handle_exceptions
    def create_block(self, block: Block) -> Result[ApiError, Block]:
        """
        Creates a _blocks in the Notion API with the values of the passed in _blocks parameter, ID, archived and in_trash
        attributes will be ignored, as they are redundant as the _blocks has non even been created yet. The _blocks will
        be attached to the parent specified in the parent attribute.

        Parameters:
            block (Block): The _blocks to create based on the values of the attributes passed in.

        Returns:
            Result[ApiError, bool]: True if the creation is successful,
                                       or a Failure containing a CustomError if the creation fails.
        """
        result = self.append_block_children(block.parent.get_parent_id(), [block])
        if isinstance(result, Failure):
            return Failure(result.failure())
        return result.unwrap()[0]

    @handle_exceptions
    def append_block_children(self, object_id: str, children_blocks: list[Block], after_block_id: str = '') -> \
            Result[ApiError, list[Block]]:
        """
        Appends children _blocks to an existing _blocks in the Notion API. By default, appends the children at the end
        of the children _blocks list or after the id of the _blocks specified in the after_block_id parameter. The id of
        the _blocks objects in the children are ignored, as these are new _blocks objects that will be created. So this
        functionality is used to create _blocks.

        From Notion Documentation:
        '
        Existing _blocks cannot be moved using this endpoint. Blocks are appended to the bottom of the parent _blocks.
        To append a _blocks in a specific place other than the bottom of the parent _blocks, use the "after"(
        after_block_id) parameter and  set its value to the ID of the _blocks that the new _blocks should be appended after.
        Once a _blocks is appended as a child, it can't be moved elsewhere via the API.
        For _blocks that allow children, we allow up to two levels of nesting in a single request.
        There is a limit of 100 _blocks children that can be appended by a single API request. Arrays of _blocks children longer than 100 will result in an error.
        '

        Parameters:
            object_id (str): The id of the _blocks to which children will be appended.
            children_blocks (list, Block): The list of children _blocks to append.
            after_block_id (str): The ID of the _blocks after which the children will be appended.
                                            If not provided, then by default, the children will be appended at the
                                            end of the parent _blocks as that is the default behavior in Notion.

        Returns:
            Result[ApiError, bool]: True if the operation is successful,
                                       or a Failure containing a CustomError if the operation fails.
        """
        children = _create_children_block_data(children_blocks, after_block_id)
        print(children)
        response = self.notion_client.append_block_children(object_id, children)
        if response.status_code != SUCCESS:
            return Failure(ApiError(message=response.text, status_code=response.status_code))
        return _parse_result(response.json())

    @handle_exceptions
    def set_block_children(self, block: Block) -> Result[ApiError, list[Block]]:
        """
        Sets the _blocks parameter object children in the Notion API to the _blocks objects in the children attribute.
        The ordering will be set based on the order of the children attribute list. Any children which are currently
        attached in notion to the _blocks and are not present in the list will be deleted. This first deletes all the
        children attached to the _blocks in the Notion and afterward appends all the children in the children attribute.

        Parameters:
            block (Block): The _blocks whose children are to be set in the Notion API.

        Returns:
            Result[ApiError, bool]: True if the operation is successful,
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

    @handle_exceptions
    def retrieve_block(self, block_id: str, retrieve_children: bool = True) -> Result[ApiError, Block]:
        """
        Retrieve a _blocks from the Notion API. By default, automatically retrieves and adds the children _blocks
        recursively to the children parameter of the resulting Block.

        Parameters:
            block_id (str): The ID of the _blocks to retrieve.
            retrieve_children (bool): Whether to retrieve and add the children _blocks to the resulting Block. If set to False the children attribute will contain an empty list

        Returns:
            Result[ApiError, Block]: A Success containing the retrieved Block if the operation is successful,
                                        or a Failure containing a CustomError if the operation fails.
        """
        response = self.notion_client.retrieve_block(block_id)
        if response.status_code != SUCCESS:
            return Failure(ApiError(response.status_code, response.text))

        block = deserialize_block(response.json())

        if block.has_children and retrieve_children:
            result = self.retrieve_block_children(block)
            if isinstance(result, Failure):
                return result

        return block

    @handle_exceptions
    def retrieve_block_children(self, block: Block, recursively: bool = True) -> Result[ApiError, Block]:
        """
         Retrieves and appends children _blocks to a given _blocks to his children attribute. Any objects in the children
         attribute of the _blocks parameter will be overwritten and removed. By default, it is set to
         recursively retrieve the children of the children _blocks as well.

         Parameters:
             block (Block): The parent _blocks whose children are to be retrieved.
             recursively (bool): Whether to retrieve the children of the children _blocks as well, by default True

         Returns:
             Result[ApiError, Block]: A Success containing the _blocks with its children if the operation is successful,
                                         or a Failure containing a CustomError if the operation fails.
         """
        block.children = []
        result = self.retrieve_children(block.id, recursively)
        if isinstance(result, Failure):
            return Failure(result.failure())
        block.children = result.unwrap()
        return block

    @handle_exceptions
    def retrieve_children(self, _id: UUID, recursively: bool = True) -> Result[ApiError, list[Block]]:
        result_children = []
        response = self.notion_client.retrieve_block_children(_id.hex)
        if response.status_code != SUCCESS:
            return Failure(ApiError(response.status_code, response.text))

        children = _access_children(response)
        for block_child in children:
            child = self.retrieve_block(_access_child_id(block_child), recursively)
            if isinstance(child, Failure):
                return Failure(child.failure())
            result_children.append(child.unwrap())

        return result_children

    @handle_exceptions
    def update_block(self, block: Block) -> Result[ApiError, Block]:
        """
         Updates a _blocks in the Notion API with the values of the passed in _blocks parameter. The id of the _blocks will be
         taken from the Block parameter

         Parameters:
             block (Block): The _blocks to update. It will be updated based on the values of the parameters of this _blocks.

         Returns:
             Result[ApiError, bool]: True if the update is successful,
                                        or a Failure containing a CustomError if the update fails.
         """
        data = block.model_dump(mode='json', exclude_none=True)
        response = self.notion_client.update_block(block.id.hex, data)
        if response.status_code != SUCCESS:
            return Failure(ApiError(response.status_code, response.text))

        return deserialize_block(response.json())

    @handle_exceptions
    def delete_block_with_id(self, block_id: str) -> Result[ApiError, bool]:
        """
         Deletes a _blocks from the Notion API with the specified ID.

         Parameters:
             block_id (str): The ID of the _blocks to delete.

         Returns:
             Result[ApiError, bool]: True if the deletion is successful,
                                        or a Failure containing a CustomError if the deletion fails.
         """
        response = self.notion_client.delete_block(block_id)
        return True if response.status_code == SUCCESS else Failure(ApiError(response.status_code, response.text))

    def delete_block(self, block: Block) -> Result[ApiError, bool]:
        """
        Deletes a _blocks from the Notion API with the specified ID container in the Block object.

        Parameters:
            block (Block): The _blocks to delete.

        Returns:
            Result[ApiError, bool]: True if the deletion is successful,
                                       or a Failure containing a CustomError if the deletion fails.
        """
        return self.delete_block_with_id(block.id.hex)
