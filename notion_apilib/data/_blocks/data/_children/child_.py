# Standard Library
from abc import ABC

# Third Party
from pydantic import BaseModel

# First Party
from ...block import Block, BlockType


class ChildAttributes(BaseModel):
    """
    Represents the attributes of a child in the Notion API.

    :param title: The title of the child.
    :type title: str
    """
    title: str


class ChildDatabase(Block):
    """
    Represents a ChildDatabase block in the Notion API.

    :param child_database: The attributes of the child database.
    :type child_database: ChildAttributes
    """
    child_database: ChildAttributes

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.CHILD_DATABASE


class ChildPage(Block):
    """
    Represents a ChildPage block in the Notion API.

    :param child_page: The attributes of the child page.
    :type child_page: ChildAttributes
    """
    child_page: ChildAttributes

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.CHILD_PAGE


__all__ = ["ChildDatabase", "ChildPage"]
