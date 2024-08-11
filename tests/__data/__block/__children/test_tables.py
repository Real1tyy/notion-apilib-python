import pytest

from notion_api.data.blocks import Table, TableRow, TableOfContents, Column
from __block.assertions import assert_block_data_is_correct, create_block_structure
from __data.utils.__structures import create_rich_text_data, assert_rich_text_structure

# Constants
HAS_COLUMN_HEADER = True
HAS_ROW_HEADER = False
TABLE_WIDTH = 3
TABLE_ROW_CONTENT = "Row content"
TABLE_OF_CONTENTS_COLOR = "gray"


@pytest.fixture
def table_block(block_data):
    def create_table_data(block_type) -> dict:
        table_data = {
            "has_column_header": HAS_COLUMN_HEADER,
            "has_row_header": HAS_ROW_HEADER,
            "table_width": TABLE_WIDTH,
        }
        data = block_data(block_type, table_data)
        return data

    return create_table_data


@pytest.fixture
def table_row_block(block_data):
    def create_table_row_data(block_type) -> dict:
        table_row_data = {
            "cells": [
                create_rich_text_data(TABLE_ROW_CONTENT, TABLE_OF_CONTENTS_COLOR)
            ],
        }
        data = block_data(block_type, table_row_data)
        return data

    return create_table_row_data


@pytest.fixture
def table_of_contents_block(block_data):
    def create_table_of_contents_data(block_type) -> dict:
        table_of_contents_data = {
            "color": TABLE_OF_CONTENTS_COLOR,
        }
        data = block_data(block_type, table_of_contents_data)
        return data

    return create_table_of_contents_data


@pytest.fixture
def column_block(block_data):
    def create_column_data(block_type) -> dict:
        column_data = {}
        data = block_data(block_type, column_data)
        return data

    return create_column_data


def test_table_structure(table_block):
    table = create_block_structure(Table, table_block)
    assert_table_data_is_correct(table)


def test_table_row_structure(table_row_block):
    table_row = create_block_structure(TableRow, table_row_block)
    assert_table_row_data_is_correct(table_row)


def test_table_of_contents_structure(table_of_contents_block):
    table_of_contents = create_block_structure(TableOfContents, table_of_contents_block)
    assert_table_of_contents_data_is_correct(table_of_contents)


def test_column_structure(column_block):
    column = create_block_structure(Column, column_block)
    assert_column_data_is_correct(column)


def assert_table_data_is_correct(data: Table):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    table_data = data.table

    assert table_data.has_column_header == HAS_COLUMN_HEADER
    assert table_data.has_row_header == HAS_ROW_HEADER
    assert table_data.table_width == TABLE_WIDTH


def assert_table_row_data_is_correct(data: TableRow):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    table_row_data = data.table_row

    assert_rich_text_structure(table_row_data.cells, TABLE_ROW_CONTENT, TABLE_OF_CONTENTS_COLOR)


def assert_table_of_contents_data_is_correct(data: TableOfContents):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    table_of_contents_data = data.table_of_contents

    assert table_of_contents_data.color == TABLE_OF_CONTENTS_COLOR


def assert_column_data_is_correct(data: Column):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    # No specific attributes to check for Column blocks.
