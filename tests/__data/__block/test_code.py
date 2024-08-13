import pytest

from notion_api.data.blocks import Code
from __block.helper import extract_create_assert_structure, extract_create_assert_serialization
from __block.assertions import assert_block_data_is_correct
from __structures.assertions import assert_rich_text_structure
from ..__structures.conftest import create_rich_text

# Constants
LANGUAGE = "python"


@pytest.fixture
def code_block(block_data, create_rich_text):
    def create_code_data(block_type) -> dict:
        CODE_DATA = {
            "caption": create_rich_text,
            "rich_text": create_rich_text,
            "language": LANGUAGE,
        }
        return block_data(block_type, CODE_DATA)

    return create_code_data


def assert_code_data_is_correct(data: Code, expected_data: dict):
    assert_block_data_is_correct(data, expected_data)
    code_data = data.code
    expected_code_data = expected_data["code"]

    assert_rich_text_structure(code_data.caption, expected_code_data["caption"])
    assert_rich_text_structure(code_data.rich_text, expected_code_data["rich_text"])
    assert code_data.language == expected_code_data["language"]


def test_block_structure(code_block):
    extract_create_assert_structure(code_block, Code, assert_code_data_is_correct)


def test_block_serialization(code_block):
    extract_create_assert_serialization(code_block, Code)
