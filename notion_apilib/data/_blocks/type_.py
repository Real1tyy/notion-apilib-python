# Standard Library
from enum import Enum


class BlockType(str, Enum):
    """
    Enum representing the various types of blocks in the Notion API.

    Attributes
    ----------
    BOOKMARK : str
        Represents a bookmark block.
    BREADCRUMB : str
        Represents a breadcrumb block.
    BULLETED_LIST_ITEM : str
        Represents a bulleted list item block.
    CALLOUT : str
        Represents a callout block.
    CHILD_DATABASE : str
        Represents a child database block.
    CHILD_PAGE : str
        Represents a child page block.
    COLUMN : str
        Represents a column block.
    COLUMN_LIST : str
        Represents a column list block.
    CODE : str
        Represents a code block.
    DIVIDER : str
        Represents a divider block.
    EMBED : str
        Represents an embed block.
    EQUATION : str
        Represents an equation block.
    FILE : str
        Represents a file block.
    HEADING_1 : str
        Represents a heading 1 block.
    HEADING_2 : str
        Represents a heading 2 block.
    HEADING_3 : str
        Represents a heading 3 block.
    IMAGE : str
        Represents an image block.
    LINK_PREVIEW : str
        Represents a link preview block.
    LINK_TO_PAGE : str
        Represents a link to page block.
    MENTION : str
        Represents a mention block.
    NUMBERED_LIST_ITEM : str
        Represents a numbered list item block.
    PARAGRAPH : str
        Represents a paragraph block.
    PDF : str
        Represents a PDF block.
    QUOTE : str
        Represents a quote block.
    SYNCED_BLOCK : str
        Represents a synced block.
    TABLE : str
        Represents a table block.
    TABLE_OF_CONTENTS : str
        Represents a table of contents block.
    TABLE_ROW : str
        Represents a table row block.
    TEMPLATE : str
        Represents a template block.
    TO_DO : str
        Represents a to-do block.
    TOGGLE : str
        Represents a toggle block.
    UNSUPPORTED : str
        Represents an unsupported block.
    VIDEO : str
        Represents a video block.
    """

    BOOKMARK = "bookmark"
    BREADCRUMB = "breadcrumb"
    BULLETED_LIST_ITEM = "bulleted_list_item"
    CALLOUT = "callout"
    CHILD_DATABASE = "child_database"
    CHILD_PAGE = "child_page"
    COLUMN = "column"
    COLUMN_LIST = "column_list"
    CODE = "code"
    DIVIDER = "divider"
    EMBED = "embed"
    EQUATION = "equation"
    FILE = "file"
    HEADING_1 = "heading_1"
    HEADING_2 = "heading_2"
    HEADING_3 = "heading_3"
    IMAGE = "image"
    LINK_PREVIEW = "link_preview"
    LINK_TO_PAGE = "link_to_page"
    MENTION = "mention"
    NUMBERED_LIST_ITEM = "numbered_list_item"
    PARAGRAPH = "paragraph"
    PDF = "pdf"
    QUOTE = "quote"
    SYNCED_BLOCK = "synced_block"
    TABLE = "table"
    TABLE_OF_CONTENTS = "table_of_contents"
    TABLE_ROW = "table_row"
    TEMPLATE = "template"
    TO_DO = "to_do"
    TOGGLE = "toggle"
    UNSUPPORTED = "unsupported"
    VIDEO = "video"
