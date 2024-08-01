from pydantic import BaseModel

from Block import Block
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
    return Code(
        object="block", archived=False, in_trash=False, parent=parent, type=BlockType.CODE, has_children=False,
        children=[], code=CodeAttributes(caption=caption, rich_text=rich_text, language=language))
