from pydantic import BaseModel

from block import Block
from structures import RichText
from type_ import BlockType


class HeadingsAttributes(BaseModel):
    """
    Attributes for heading _blocks.

    :param rich_text: List of rich text elements.
    :param color: Color of the heading text.
    :param is_toggleable: Whether the heading is toggleable.
    """
    rich_text: list[RichText]
    color: str
    is_toggleable: bool


class Heading1(Block):
    """
    Heading 1 block.

    :param heading_1: Attributes for the heading 1 block.
    """
    heading_1: HeadingsAttributes

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.HEADING_1


class Heading2(Block):
    """
    Heading 2 _blocks.

    :param heading_2: Attributes for the heading 2 _blocks.
    """
    heading_2: HeadingsAttributes

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.HEADING_2


class Heading3(Block):
    """
    Heading 3 _blocks.

    :param heading_3: Attributes for the heading 3 _blocks.
    """
    heading_3: HeadingsAttributes

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.HEADING_3


__all__ = ["Heading1", "Heading2", "Heading3"]
