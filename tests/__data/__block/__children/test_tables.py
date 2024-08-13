import pytest

from __block.helper import extract_create_assert_structure, extract_create_assert_serialization
from notion_api.data.blocks import Table, TableRow, TableOfContents, Column
from __block.assertions import assert_block_data_is_correct
from __structures.assertions import assert_rich_text_structure

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
        table_row_data = {
            "cells": create_rich_text
        }
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


def test_table_block_structure(table_block):
    extract_create_assert_structure(table_block, Table, assert_table_data_is_correct)


def test_table_row_block_structure(table_row_block):
    extract_create_assert_structure(table_row_block, TableRow, assert_table_row_data_is_correct)


def test_table_of_contents_block_structure(table_of_contents_block):
    extract_create_assert_structure(table_of_contents_block, TableOfContents, assert_table_of_contents_data_is_correct)


def test_column_block_structure(column_block):
    extract_create_assert_structure(column_block, Column, assert_column_data_is_correct)


def test_table_block_serialization(table_block):
    extract_create_assert_serialization(table_block, Table)


def test_table_row_block_serialization(table_row_block):
    extract_create_assert_serialization(table_row_block, TableRow)


def test_table_of_contents_block_serialization(table_of_contents_block):
    extract_create_assert_serialization(table_of_contents_block, TableOfContents)


def test_column_block_serialization(column_block):
    extract_create_assert_serialization(column_block, Column)
