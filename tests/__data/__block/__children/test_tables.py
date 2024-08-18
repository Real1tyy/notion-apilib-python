# Third Party
import pytest

# First Party
from notion_apilib.data.blocks import Column, Table, TableOfContents, TableRow
from tests.__data.__block.assertions import assert_block_data_is_correct
from tests.__data.__block.helper import (
    extract_create_assert_serialization,
    extract_create_assert_structure,
)
from tests.__data.__structures.assertions import assert_rich_text_structure

# Constants
HAS_COLUMN_HEADER = True
HAS_ROW_HEADER = False
TABLE_WIDTH = 3
TABLE_OF_CONTENTS_COLOR = "gray"


@pytest.fixture
def table_block(block_data):
    def create_table_data(block_type) -> dict:
        table_data = {
            "has_column_header": HAS_COLUMN_HEADER,
            "has_row_header": HAS_ROW_HEADER,
            "table_width": TABLE_WIDTH,
        }
        return block_data(block_type, table_data)

    return create_table_data


@pytest.fixture
def table_row_block(block_data, create_rich_text):
    def create_table_row_data(block_type) -> dict:
        table_row_data = {"cells": create_rich_text}
        return block_data(block_type, table_row_data)

    return create_table_row_data


@pytest.fixture
def table_of_contents_block(block_data):
    def create_table_of_contents_data(block_type) -> dict:
        table_of_contents_data = {
            "color": TABLE_OF_CONTENTS_COLOR,
        }
        return block_data(block_type, table_of_contents_data)

    return create_table_of_contents_data


@pytest.fixture
def column_block(block_data):
    def create_column_data(block_type) -> dict:
        column_data = {}
        return block_data(block_type, column_data)

    return create_column_data


def assert_table_data_is_correct(data: Table, expected_data: dict):
    assert_block_data_is_correct(data, expected_data)
    table_data = data.table
    expected_table_data = expected_data["table"]
    assert table_data.has_column_header == expected_table_data["has_column_header"]
    assert table_data.has_row_header == expected_table_data["has_row_header"]
    assert table_data.table_width == expected_table_data["table_width"]


def assert_table_row_data_is_correct(data: TableRow, expected_data: dict):
    assert_block_data_is_correct(data, expected_data)
    assert_rich_text_structure(data.table_row.cells, expected_data["table_row"]["cells"])


def assert_table_of_contents_data_is_correct(data: TableOfContents, expected_data: dict):
    assert_block_data_is_correct(data, expected_data)
    assert data.table_of_contents.color == expected_data["table_of_contents"]["color"]


def assert_column_data_is_correct(data: Column, expected_data: dict):
    assert_block_data_is_correct(data, expected_data)


@pytest.mark.parametrize(
    "block_fixture, block_class, assert_func",
    [
        ("table_block", Table, assert_table_data_is_correct),
        ("table_row_block", TableRow, assert_table_row_data_is_correct),
        (
            "table_of_contents_block",
            TableOfContents,
            assert_table_of_contents_data_is_correct,
        ),
        ("column_block", Column, assert_column_data_is_correct),
    ],
)
def test_block_structure(request, block_fixture, block_class, assert_func):
    block_data = request.getfixturevalue(block_fixture)
    extract_create_assert_structure(block_data, block_class, assert_func)


@pytest.mark.parametrize(
    "block_fixture, block_class",
    [
        ("table_block", Table),
        ("table_row_block", TableRow),
        ("table_of_contents_block", TableOfContents),
        ("column_block", Column),
    ],
)
def test_block_serialization(request, block_fixture, block_class):
    block_data = request.getfixturevalue(block_fixture)
    extract_create_assert_serialization(block_data, block_class)
