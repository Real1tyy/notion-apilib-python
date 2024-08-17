# Third Party
from pydantic import BaseModel

# First Party
from notion_apilib.data.structures import RichText

from ..block import Block, BlockType


class CodeAttributes(BaseModel):
    """
    Attributes for a code block.

    :param caption: A list of RichText objects representing the caption of the code block.
    :type caption: list[RichText]
    :param rich_text: A list of RichText objects representing the code content.
    :type rich_text: list[RichText]
    :param language: The programming language of the code.
    :type language: str
    """
    caption: list[RichText]
    rich_text: list[RichText]
    language: str


class Code(Block):
    """
    Represents a Code block.

    :param code: Attributes for the code block.
    :type code: CodeAttributes
    """
    code: CodeAttributes

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.CODE


__all__ = ["Code"]
