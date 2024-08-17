# Standard Library

# Third Party
from pydantic import BaseModel

from notion_apilib.data.structures import RichText
# First Party
from ...block import Block, BlockType


class TableAttributes(BaseModel):
    """
    Attributes for table _blocks.

    :param has_column_header: Whether the table has a column header.
    :param has_row_header: Whether the table has a row header.
    :param table_width: The width of the table.
    """
    has_column_header: bool
    has_row_header: bool
    table_width: int


class Table(Block):
    """
    Table _blocks.

    :param table: Attributes for the table _blocks.
    """
    table: TableAttributes

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.TABLE


class TableRowAttributes(BaseModel):
    """
    Attributes for table row _blocks.

    :param cells: List of rich text elements representing the cells.
    """
    cells: list[RichText]


class TableRow(Block):
    """
    Table row _blocks.

    :param table_row: Attributes for the table row _blocks.
    """
    table_row: TableRowAttributes

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.TABLE_ROW


class TableOfContentsAttributes(BaseModel):
    """
    Attributes for table of contents _blocks.

    :param color: Color of the table of contents text.
    """
    color: str


class TableOfContents(Block):
    """
    Table of contents _blocks.

    :param table_of_contents: Attributes for the table of contents _blocks.
    """
    table_of_contents: TableOfContentsAttributes

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.TABLE_OF_CONTENTS


class Column(Block):
    """
    Column _blocks.
    """

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.COLUMN


__all__ = ['Table', 'TableRow', 'TableOfContents', 'Column']
