from pydantic import BaseModel

from Block import Block
from Parent import Parent
from RichText import RichText


class BookmarkAttributes(BaseModel):
    url: str
    caption: list[RichText]


class Bookmark(Block):
    bookmark: BookmarkAttributes


def create_bookmark_object(parent: Parent, url: str, caption: list[str]) -> Bookmark:
    """
    Factory method to create Bookmark object
    :param parent: parent object
    :param caption: caption
    :param url: url
    :return: newly created Code Object
    """
    return Bookmark(
        object="block", archived=False, in_trash=False, parent=parent, type=BlockType.CODE, has_children=False,
        children=[], code=CodeAttributes(caption=caption, rich_text=rich_text, language=language))
