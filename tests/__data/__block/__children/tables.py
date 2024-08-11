import pytest

from notion_api.data.blocks import Table, TableRow, TableOfContents, Column, BlockType
from ....__data.block import add_block_data, assert_block_data_is_correct, create_block_structure
from ....__data.utils import create_rich_text_data, assert_rich_text_data

# Constants
HAS_COLUMN_HEADER = True
HAS_ROW_HEADER = False
TABLE_WIDTH = 3
TABLE_ROW_CONTENT = "Row content"
TABLE_OF_CONTENTS_COLOR = "gray"


def _create_table_data(block_type) -> dict:
    @add_block_data(block_type)
    def table_data():
        return {
            "has_column_header": HAS_COLUMN_HEADER,
            "has_row_header": HAS_ROW_HEADER,
            "table_width": TABLE_WIDTH,
        }

    return table_data()


def _create_table_row_data(block_type) -> dict:
    @add_block_data(block_type)
    def table_row_data():
        return {
            "cells": [
                create_rich_text_data(TABLE_ROW_CONTENT, TABLE_OF_CONTENTS_COLOR)
            ],
        }

    return table_row_data()


def _create_table_of_contents_data(block_type) -> dict:
    @add_block_data(block_type)
    def table_of_contents_data():
        return {
            "color": TABLE_OF_CONTENTS_COLOR,
        }

    return table_of_contents_data()


def _create_column_data(block_type) -> dict:
    @add_block_data(block_type)
    def column_data():
        return {}

    return column_data()


@pytest.fixture
def table_block():
    return _create_table_data


@pytest.fixture
def table_row_block():
    return _create_table_row_data


@pytest.fixture
def table_of_contents_block():
    return _create_table_of_contents_data


@pytest.fixture
def column_block():
    return _create_column_data


def test_table_structure(table_block):
    item = create_block_structure(Table, table_block)
    assert_table_data_correct(item)


def test_table_row_structure(table_row_block):
    item = create_block_structure(TableRow, table_row_block)
    assert_table_row_data_correct(item)


def test_table_of_contents_structure(table_of_contents_block):
    item = create_block_structure(TableOfContents, table_of_contents_block)
    assert_table_of_contents_data_correct(item)


def test_column_structure(column_block):
    item = create_block_structure(Column, column_block)
    assert_column_data_correct(item)


def assert_table_data_correct(data: Table):
    block_type = Table.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    table_data = data.table

    assert table_data.has_column_header == HAS_COLUMN_HEADER
    assert table_data.has_row_header == HAS_ROW_HEADER
    assert table_data.table_width == TABLE_WIDTH


def assert_table_row_data_correct(data: TableRow):
    block_type = TableRow.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    table_row_data = data.table_row

    assert len(table_row_data.cells) == 1
    cell = table_row_data.cells[0]

    assert_rich_text_data(cell, TABLE_ROW_CONTENT, TABLE_OF_CONTENTS_COLOR)


def assert_table_of_contents_data_correct(data: TableOfContents):
    block_type = TableOfContents.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    table_of_contents_data = data.table_of_contents

    assert table_of_contents_data.color == TABLE_OF_CONTENTS_COLOR


def assert_column_data_correct(data: Column):
    block_type = Column.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    # No specific attributes to check for Column blocks.
