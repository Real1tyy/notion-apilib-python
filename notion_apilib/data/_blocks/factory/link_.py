# First Party
from ._general import _create_block
from ..data import Bookmark, Embed, LinkPreview, block_structures
from notion_apilib.data.structures import Parent, RichText


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
        block_type_specific_params=block_structures.BookmarkAttributes(
            caption=caption, url=url
        ),
    )


def create_embed(parent: "Parent", url: str) -> Embed:
    """
    Factory method to create Embed object
    :param parent: parent object
    :param url: URL for the embed
    :return: newly created Embed Object
    """
    return _create_block(
        Embed,
        parent=parent,
        block_type_specific_params=block_structures.EmbedAttributes(url=url),
    )


def create_link_preview(parent: "Parent", url: str) -> LinkPreview:
    """
    Factory method to create LinkPreview object
    :param parent: parent object
    :param url: URL for the link preview
    :return: newly created LinkPreview Object
    """
    return _create_block(
        LinkPreview,
        parent=parent,
        block_type_specific_params=block_structures.LinkPreviewAttributes(url=url),
    )


__all__ = ["create_bookmark", "create_embed", "create_link_preview"]
