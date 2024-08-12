import pytest

from __block.assertions import assert_block_data_is_correct, create_block_object, assert_serialization_to_json, \
    extract_block_data
from __block.helper import extract_create_assert_structure, extract_create_assert_serialization
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
        return block_data(block_type, HEADING_DATA)

    return create_heading_data


@pytest.mark.parametrize("heading_class", [Heading1, Heading2, Heading3])
def test_heading_structure(heading_block, heading_class):
    extract_create_assert_structure(heading_block, heading_class, assert_heading_data_is_correct)


@pytest.mark.parametrize("heading_class", [Heading1, Heading2, Heading3])
def test_heading_serialization(heading_block, heading_class):
    extract_create_assert_serialization(heading_block, heading_class)


def assert_heading_data_is_correct(data, expected_data):
    assert_block_data_is_correct(data, expected_data)
    block_type = data.__class__.get_associated_block_type()
    heading_data = getattr(data, f"{block_type.value}")
    heading_expected_data = expected_data[block_type.value]

    assert_rich_text_structure(heading_data.rich_text, heading_expected_data["rich_text"])
    assert heading_data.color == heading_expected_data["color"]
    assert heading_data.is_toggleable == heading_expected_data["is_toggleable"]
