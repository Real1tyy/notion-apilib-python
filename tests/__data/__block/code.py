import pytest

from notion_api.data.blocks import Code, BlockType
from __data.block import add_block_data, assert_block_data_is_correct, create_block_structure
from __data.utils import create_rich_text_data, assert_rich_text_data

# Constants
CAPTION_CONTENT = "Code snippet caption"
CODE_CONTENT = "print('Hello, World!')"
LANGUAGE = "python"
CAPTION_COLOR = "gray"
CODE_COLOR = "black"


def _create_code_data(block_type) -> dict:
    @add_block_data(block_type)
    def code_data():
        return {
            "caption": [
                create_rich_text_data(CAPTION_CONTENT, CAPTION_COLOR)
            ],
            "rich_text": [
                create_rich_text_data(CODE_CONTENT, CODE_COLOR)
            ],
            "language": LANGUAGE,
        }

    return code_data()


@pytest.fixture
def code_block():
    return _create_code_data


def test_code_structure(code_block):
    item = create_block_structure(Code, code_block)
    assert_code_data_correct(item)


def assert_code_data_correct(data: Code):
    block_type = Code.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    code_data = data.code

    # Verify caption
    assert len(code_data.caption) == 1
    caption = code_data.caption[0]
    assert_rich_text_data(caption, CAPTION_CONTENT, CAPTION_COLOR)

    # Verify code content
    assert len(code_data.rich_text) == 1
    code_text = code_data.rich_text[0]
    assert_rich_text_data(code_text, CODE_CONTENT, CODE_COLOR)

    # Verify language
    assert code_data.language == LANGUAGE
