# Standard Library
from typing import Optional

# First Party
from notion_api.data._blocks._data.children.tables import (
    Column,
    Table,
    TableAttributes,
    TableOfContents,
    TableOfContentsAttributes,
    TableRow,
    TableRowAttributes,
)
from notion_api.data._blocks._factory.general import _create_block
from notion_api.data._blocks.block import Block
from notion_api.data.structures import Parent, RichText


def create_table(
        parent: Parent, has_column_header: bool, has_row_header: bool, table_width: int,
        children: Optional[list[Block]] = None) -> Table:
    """
    Factory method to create a Table object.

    :param parent: The parent object.
    :param has_column_header: Whether the table has a column header.
    :param has_row_header: Whether the table has a row header.
    :param table_width: The width of the table.
    :param children: List of child _blocks (optional).
    :return: A new Table object.
    """
    return _create_block(
        Table,
        parent=parent,
        block_type_specific_params=TableAttributes(
            has_column_header=has_column_header,
            has_row_header=has_row_header,
            table_width=table_width
        ),
        children=children
    )


def create_table_row(parent: Parent, cells: list[RichText], children: Optional[list[Block]] = None) -> TableRow:
    """
    Factory method to create a TableRow object.

    :param parent: The parent object.
    :param cells: The rich text content of the cells.
    :param children: List of child _blocks (optional).
    :return: A new TableRow object.
    """
    return _create_block(
        TableRow,
        parent=parent,
        block_type_specific_params=TableRowAttributes(
            cells=cells
        ),
        children=children
    )


def create_table_of_contents(
        parent: Parent, color: str, children: Optional[list[Block]] = None) -> TableOfContents:
    """
    Factory method to create a TableOfContents object.

    :param parent: The parent object.
    :param color: The color of the table of contents text.
    :param children: List of child _blocks (optional).
    :return: A new TableOfContents object.
    """
    return _create_block(
        TableOfContents,
        parent=parent,
        block_type_specific_params=TableOfContentsAttributes(
            color=color
        ),
        children=children
    )


def create_column(parent: Parent, children: Optional[list[Block]] = None) -> Column:
    """
    Factory method to create a Column object.

    :param parent: The parent object.
    :param children: List of child _blocks (optional).
    :return: A new Column object.
    """
    return _create_block(
        Column,
        parent=parent,
        children=children,
    )


__all__ = [
    'create_column', 'create_table', 'create_table_row', 'create_table_of_contents'
]
