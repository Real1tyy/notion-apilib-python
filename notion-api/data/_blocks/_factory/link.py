from Parent import Parent
from RichText import RichText
from _data.link import Bookmark, BookmarkAttributes, Embed, EmbedAttributes, LinkPreview, LinkPreviewAttributes
from block import _create_block
from type import BlockType


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
