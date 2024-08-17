# Standard Library
from dataclasses import dataclass
from uuid import UUID

# First Party
from ._api_requests import NotionAPIBlocksClient
from ._utils import (
    _create_children_json_payload,
    _get_child_id_from_json,
    _get_children_from_json,
    _handle_pagination,
    _parse_and_serialize_result,
)
from notion_apilib.data.blocks import Block, deserialize_block


@dataclass
class NotionBlockProvider:
    """
    Provides API methods to interact with Notion API block endpoints using and returning DSL block objects.

    """

    notion_client: NotionAPIBlocksClient

    def create_block(self, block: Block) -> Block:
        """
        Creates a block in the Notion API with the values of the passed in block parameter. ID, archived, and in_trash
        attributes will be ignored, as they are redundant since the block has not even been created yet. The block will
        be attached to the parent specified in the parent attribute.

        Parameters:
            block (Block): The block to create based on the values of the attributes passed in.

        Returns:
            Block: The created Block object.

        Raises:
            ValueError: If the deserialization of the response fails due to an invalid schema.
            ResponseException: If the Notion API returns an error status code.
        """
        return self.append_block_children(block.parent.get_parent_id(), [block])

    def append_block_children(
            self, object_id: str, children_blocks: list[Block], after_block_id: str = ""
    ) -> Block:
        """
        Appends children blocks to an existing block in the Notion API. By default, appends the children at the end
        of the children block list or after the id of the block specified in the after_block_id parameter. The id of
        the block objects in the children are ignored, as these are new block objects that will be created.

        Parameters:
            object_id (str): The id of the block to which children will be appended.
            children_blocks (list[Block]): The list of children blocks to append.
            after_block_id (str): The ID of the block after which the children will be appended.
                                  If not provided, the children will be appended at the end of the parent block.

        Returns:
            Block: The updated Block object with the new children.

        Raises:
            ValueError: If the deserialization of the response fails due to an invalid schema.
            ResponseException: If the Notion API returns an error status code.
        """
        block = self.retrieve_block(object_id)
        children = _create_children_json_payload(children_blocks, after_block_id)
        response = self.notion_client.append_block_children(object_id, children)
        block.children = _parse_and_serialize_result(response.json())
        return block

    def set_block_children(self, block: Block) -> Block:
        """
        Sets the block parameter object children in the Notion API to the block objects in the children attribute.
        The ordering will be set based on the order of the children attribute list. Any children which are currently
        attached in Notion to the block and are not present in the list will be deleted. This first deletes all the
        children attached to the block in the Notion and afterward appends all the children in the children attribute.

        Parameters:
            block (Block): The block whose children are to be set in the Notion API.

        Returns:
            Block: The updated Block object with the new children.

        Raises:
            ValueError: If the deserialization of the response fails due to an invalid schema.
            ResponseException: If the Notion API returns an error status code.
        """
        notion_block = self.retrieve_block(block.id.hex)
        [self.delete_block(child) for child in notion_block.children]
        block.children = self.append_block_children(block.id.hex, block.children)
        return block

    def retrieve_block(self, block_id: str, retrieve_children: bool = True) -> Block:
        """
        Retrieves a block from the Notion API. By default, automatically retrieves and adds the children blocks
        recursively to the children parameter of the resulting Block.

        Parameters:
            block_id (str): The ID of the block to retrieve.
            retrieve_children (bool): Whether to retrieve and add the children blocks to the resulting Block.
                                      If set to False, the children attribute will contain an empty list.

        Returns:
            Block: The retrieved Block object.

        Raises:
            ValueError: If the deserialization of the response fails due to an invalid schema.
            ResponseException: If the Notion API returns an error status code.
        """
        response = self.notion_client.retrieve_block(block_id)
        block = deserialize_block(response.json())
        if block.has_children and retrieve_children:
            self.retrieve_block_children(block)
        return block

    def retrieve_block_children(self, block: Block, recursively: bool = True) -> Block:
        """
        Retrieves and appends children blocks to a given block's children attribute. Any objects in the children
        attribute of the block parameter will be overwritten and removed. By default, it is set to
        recursively retrieve the children of the children blocks as well.

        Parameters:
            block (Block): The parent block whose children are to be retrieved.
            recursively (bool): Whether to retrieve the children of the children blocks as well, by default True.

        Returns:
            Block: The block with its children retrieved.

        Raises:
            ValueError: If the deserialization of the response fails due to an invalid schema.
            ResponseException: If the Notion API returns an error status code.
        """
        block.children = self._retrieve_children(block.id, recursively)
        return block

    def _retrieve_children(self, id_: UUID, recursively: bool = True) -> list[Block]:
        """
        Helper function to retrieve children blocks.

        Parameters:
            id_ (UUID): The ID of the block whose children are to be retrieved.
            recursively (bool): Whether to recursively retrieve children of the children blocks.

        Returns:
            list[Block]: A list of retrieved Block objects.

        Raises:
            ValueError: If the deserialization of the response fails due to an invalid schema.
            ResponseException: If the Notion API returns an error status code.
        """
        response = self.notion_client.retrieve_block_children(id_.hex, {})
        children_data = _get_children_from_json(response)
        new_children = [
            self.retrieve_block(_get_child_id_from_json(child), recursively)
            for child in children_data
        ]
        return _handle_pagination(
            new_children,
            response,
            self._retrieve_children_paginated,
            id_=id_,
            recursively=recursively,
            children=new_children,
        )

    def _retrieve_children_paginated(
            self,
            id_: UUID,
            next_cursor: str,
            children: list[Block],
            recursively: bool = True,
    ) -> list[Block]:
        """
        Helper function to handle paginated retrieval of children blocks.

        Parameters:
            id_ (UUID): The ID of the block whose children are being retrieved.
            next_cursor (str): The cursor indicating the next page of results.
            children (list[Block]): The current list of retrieved children blocks.
            recursively (bool): Whether to recursively retrieve children of the children blocks.

        Returns:
            list[Block]: A list of retrieved Block objects with pagination handled.

        Raises:
            ValueError: If the deserialization of the response fails due to an invalid schema.
            ResponseException: If the Notion API returns an error status code.
        """
        data = {"start_cursor": next_cursor}
        response = self.notion_client.retrieve_block_children(id_.hex, data)
        children_data = _get_children_from_json(response)
        children.extend(
            [
                self.retrieve_block(_get_child_id_from_json(child), recursively)
                for child in children_data
            ]
        )
        return _handle_pagination(
            children,
            response,
            self._retrieve_children_paginated,
            id_=id_,
            recursively=recursively,
            children=children,
        )

    def update_block(self, block: Block) -> Block:
        """
        Updates a block in the Notion API with the values of the passed in block parameter. The ID of the block will be
        taken from the Block parameter.

        Parameters:
            block (Block): The block to update. It will be updated based on the values of the parameters of this block.

        Returns:
            Block: The updated Block object.

        Raises:
            ValueError: If the deserialization of the response fails due to an invalid schema.
            ResponseException: If the Notion API returns an error status code.
        """
        data = block.model_dump(mode="json", exclude_none=True)
        response = self.notion_client.update_block(block.id.hex, data)
        return deserialize_block(response.json())

    def delete_block_with_id(self, block_id: str) -> None:
        """
        Deletes a block from the Notion API with the specified ID.

        Parameters:
            block_id (str): The ID of the block to delete.

        Raises:
            ResponseException: If the Notion API returns an error status code.
        """
        self.notion_client.delete_block(block_id)

    def delete_block(self, block: Block) -> None:
        """
        Deletes a block from the Notion API using a Block object.

        Parameters:
            block (Block): The block to delete.

        Raises:
            ResponseException: If the Notion API returns an error status code.
        """
        return self.delete_block_with_id(block.id.hex)
