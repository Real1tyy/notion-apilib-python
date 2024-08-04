# Third Party
from pydantic import BaseModel

from _data.RichText import RichText
from block import Block


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
