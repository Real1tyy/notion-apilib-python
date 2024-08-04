from pydantic import BaseModel

from Block import Block, _create_block
from BlockType import BlockType
from Parent import Parent
from RichText import RichText


class BookmarkAttributes(BaseModel):
    url: str
    caption: list[RichText]


class Bookmark(Block):
    bookmark: BookmarkAttributes


def create_bookmark(parent: Parent, url: str, caption: list[RichText]) -> Bookmark:
    """
    Factory method to create Bookmark object
    :param parent: parent object
    :param caption: caption
    :param url: url
    :return: newly created Code Object
    """
    return _create_block(
        Bookmark,
        parent=parent,
        block_type=BlockType.CODE,
        bookmark=BookmarkAttributes(caption=caption, url=url)
    )
