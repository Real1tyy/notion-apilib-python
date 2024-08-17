# Third Party
from pydantic import BaseModel

# First Party
from notion_apilib.data.structures import RichText

from ..block import Block, BlockType


class BookmarkAttributes(BaseModel):
    """
    Attributes for a bookmark block.

    :param url: The URL of the bookmark.
    :type url: str
    :param caption: A list of RichText objects representing the caption of the bookmark.
    :type caption: list[RichText]
    """
    url: str
    caption: list[RichText]


class Bookmark(Block):
    """
    Represents a Bookmark block.

    :param bookmark: Attributes for the bookmark block.
    :type bookmark: BookmarkAttributes
    """
    bookmark: BookmarkAttributes

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.BOOKMARK


class EmbedAttributes(BaseModel):
    """
    Attributes for an embed block.

    :param url: The URL of the embedded content.
    :type url: str
    """
    url: str


class Embed(Block):
    """
    Represents an Embed block.

    :param embed: Attributes for the embed block.
    :type embed: EmbedAttributes
    """
    embed: EmbedAttributes

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.EMBED


class LinkPreviewAttributes(BaseModel):
    """
    Attributes for a link preview block.

    :param url: The URL of the link to preview.
    :type url: str
    """
    url: str


class LinkPreview(Block):
    """
    Represents a Link Preview block.

    :param link_preview: Attributes for the link preview block.
    :type link_preview: LinkPreviewAttributes
    """
    link_preview: LinkPreviewAttributes

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.LINK_PREVIEW


__all__ = ["Embed", "LinkPreview", "Bookmark"]
