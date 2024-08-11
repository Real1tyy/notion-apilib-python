import pytest

from __block.assertions import assert_block_data_is_correct, create_block_structure, assert_serialization_to_json
from notion_api.data.blocks import Heading1, Heading2, Heading3
from __data.utils.__structures import create_rich_text_data, assert_rich_text_structure

RICH_TEXT_CONTENT = "Lacinato kale"
RICH_TEXT_COLOR = "green"
IS_TOGGLEABLE = False

HEADING_DATA = {
    "rich_text": [
        create_rich_text_data(RICH_TEXT_CONTENT, RICH_TEXT_COLOR)
    ],
    "color": RICH_TEXT_COLOR,
    "is_toggleable": IS_TOGGLEABLE,
}


@pytest.fixture
def heading_block(block_data):
    def create_heading_data(block_type) -> dict:
        data = block_data(block_type, HEADING_DATA)
        return data

    return create_heading_data


@pytest.mark.parametrize("heading_class", [Heading1, Heading2, Heading3])
def test_heading_structure(heading_block, heading_class):
    heading = create_block_structure(heading_class, heading_block)
    assert_heading_data_correct(heading)


@pytest.mark.parametrize("heading_class", [Heading1, Heading2, Heading3])
def test_heading_serialization(heading_block, heading_class):
    heading = create_block_structure(heading_class, heading_block)
    assert_serialization_to_json(heading, HEADING_DATA)


def assert_heading_data_correct(data):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    heading_data = getattr(data, f"{block_type.value}")

    assert_rich_text_structure(heading_data.rich_text, RICH_TEXT_CONTENT, RICH_TEXT_COLOR)

    assert heading_data.color == RICH_TEXT_COLOR
    assert heading_data.is_toggleable is IS_TOGGLEABLE
