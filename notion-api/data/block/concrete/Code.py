from pydantic import BaseModel

from Block import Block, _create_block_object
from BlockType import BlockType
from Parent import Parent
from RichText import RichText


class CodeAttributes(BaseModel):
    caption: list[RichText]
    rich_text: list[RichText]
    language: str


class Code(Block):
    code: CodeAttributes


def create_code_object(parent: Parent, caption: list[RichText], rich_text: list[RichText], language: str) -> Code:
    """
    Factory method to create Code object
    :param parent: parent object
    :param caption: caption
    :param rich_text: rich text
    :param language: language
    :return: newly created Code Object
    """
    return _create_block_object(
        Code,
        parent=parent,
        block_type=BlockType.CODE,
        code=CodeAttributes(caption=caption, rich_text=rich_text, language=language)
    )