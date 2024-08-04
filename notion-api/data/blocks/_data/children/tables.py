# Standard Library

from pydantic import BaseModel

from RichText import RichText
# Third Party
from blocks.block import Block


class TableAttributes(BaseModel):
    """
    Attributes for table blocks.

    :param has_column_header: Whether the table has a column header.
    :param has_row_header: Whether the table has a row header.
    :param table_width: The width of the table.
    """
    has_column_header: bool
    has_row_header: bool
    table_width: int


class Table(Block):
    """
    Table blocks.

    :param table: Attributes for the table blocks.
    """
    table: TableAttributes


class TableRowAttributes(BaseModel):
    """
    Attributes for table row blocks.

    :param cells: List of rich text elements representing the cells.
    """
    cells: list[RichText]


class TableRow(Block):
    """
    Table row blocks.

    :param table_row: Attributes for the table row blocks.
    """
    table_row: TableRowAttributes


class TableOfContentsAttributes(BaseModel):
    """
    Attributes for table of contents blocks.

    :param color: Color of the table of contents text.
    """
    color: str


class TableOfContents(Block):
    """
    Table of contents blocks.

    :param table_of_contents: Attributes for the table of contents blocks.
    """
    table_of_contents: TableOfContentsAttributes


class Column(Block):
    """
    Column blocks.
    """
    pass
