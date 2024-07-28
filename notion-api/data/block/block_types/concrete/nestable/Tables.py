from pydantic import BaseModel

from Block import Block
from RichText import RichText


class TableAttributes(BaseModel):
    has_column_header: bool
    has_row_header: bool
    table_width: int


class Table(Block):
    table: TableAttributes


class TableRowAttributes(BaseModel):
    cells: list[RichText]


class TableRow(Block):
    table_row: TableRowAttributes


class TableOfContentsAttributes(BaseModel):
    color: str


class TableOfContents(Block):
    table_of_contents: TableOfContentsAttributes


class Column(Block):
    pass
