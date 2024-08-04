# Third Party
from pydantic import BaseModel

from Parent import Parent
from RichText import RichText
from block import Block, _create_block
from type import BlockType


class CodeAttributes(BaseModel):
    caption: list[RichText]
    rich_text: list[RichText]
    language: str


class Code(Block):
    code: CodeAttributes


def create_code(parent: Parent, caption: list[RichText], rich_text: list[RichText], language: str) -> Code:
    """
    Factory method to create Code object
    :param parent: parent object
    :param caption: caption
    :param rich_text: rich text
    :param language: language
    :return: newly created Code Object
    """
    return _create_block(
        Code,
        parent=parent,
        block_type=BlockType.CODE,
        code=CodeAttributes(caption=caption, rich_text=rich_text, language=language)
    )
