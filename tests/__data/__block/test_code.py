import pytest

from notion_api.data.blocks import Code
from __block.assertions import assert_block_data_is_correct, create_block_structure
from __data.utils.__structures import create_rich_text_data, assert_rich_text_structure

# Constants
CAPTION_CONTENT = "Code snippet caption"
CODE_CONTENT = "print('Hello, World!')"
LANGUAGE = "python"
CAPTION_COLOR = "gray"
CODE_COLOR = "black"


@pytest.fixture
def code_block(block_data):
    def create_code_data(block_type) -> dict:
        code_data = {
            "caption": [
                create_rich_text_data(CAPTION_CONTENT, CAPTION_COLOR)
            ],
            "rich_text": [
                create_rich_text_data(CODE_CONTENT, CODE_COLOR)
            ],
            "language": LANGUAGE,
        }
        data = block_data(block_type, code_data)
        return data

    return create_code_data


def test_code_structure(code_block):
    code = create_block_structure(Code, code_block)
    assert_code_data_is_correct(code)


def assert_code_data_is_correct(data: Code):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    code_data = data.code

    assert_rich_text_structure(code_data.caption, CAPTION_CONTENT, CAPTION_COLOR)
    assert_rich_text_structure(code_data.rich_text, CODE_CONTENT, CODE_COLOR)

    assert code_data.language == LANGUAGE
