import pytest

from notion_api.data.blocks import Code
from __block.helper import extract_create_assert_structure, extract_create_assert_serialization
from __block.assertions import assert_block_data_is_correct
from __data.utils.__structures import create_rich_text_data, assert_rich_text_structure

# Constants
CAPTION_CONTENT = "Code snippet caption"
CODE_CONTENT = "print('Hello, World!')"
LANGUAGE = "python"
CAPTION_COLOR = "gray"
CODE_COLOR = "black"

CODE_DATA = {
    "caption": [
        create_rich_text_data(CAPTION_CONTENT, CAPTION_COLOR)
    ],
    "rich_text": [
        create_rich_text_data(CODE_CONTENT, CODE_COLOR)
    ],
    "language": LANGUAGE,
}


@pytest.fixture
def code_block(block_data):
    def create_code_data(block_type) -> dict:
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
