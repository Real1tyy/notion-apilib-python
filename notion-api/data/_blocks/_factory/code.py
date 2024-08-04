from _data.Parent import Parent
from _data.RichText import RichText
from _data.code import Code, CodeAttributes
from block import _create_block
from type import BlockType


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
