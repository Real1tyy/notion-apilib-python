# Third Party
from pydantic import BaseModel

from Parent import Parent
from RichText import RichText
from block import Block, _create_block
from type import BlockType


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


class EmbedAttributes(BaseModel):
    url: str


class Embed(Block):
    embed: EmbedAttributes


def create_embed(parent: Parent, url: str) -> Embed:
    """
    Factory method to create Embed object
    :param parent: parent object
    :param url: URL for the embed
    :return: newly created Embed Object
    """
    return _create_block(
        Embed,
        parent=parent,
        block_type=BlockType.EMBED,
        embed=EmbedAttributes(url=url)
    )


class LinkPreviewAttributes(BaseModel):
    url: str


class LinkPreview(Block):
    link_preview: LinkPreviewAttributes


def create_link_preview(parent: Parent, url: str) -> LinkPreview:
    """
    Factory method to create LinkPreview object
    :param parent: parent object
    :param url: URL for the link preview
    :return: newly created LinkPreview Object
    """
    return _create_block(
        LinkPreview,
        parent=parent,
        block_type=BlockType.LINK_PREVIEW,
        link_preview=LinkPreviewAttributes(url=url)
    )
