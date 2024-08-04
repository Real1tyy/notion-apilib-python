# Standard Library

from pydantic import BaseModel

from _data.RichText import RichText
# Third Party
from block import Block


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


class Column(Block):
    """
    Column _blocks.
    """
    pass
