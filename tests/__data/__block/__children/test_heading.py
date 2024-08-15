import pytest

from tests.__data.__block.assertions import assert_block_data_is_correct
from tests.__data.__block.helper import extract_create_assert_structure, extract_create_assert_serialization
from notion_api.data.blocks import Heading1, Heading2, Heading3
from tests.__data.__structures.assertions import assert_rich_text_structure

IS_TOGGLEABLE = False


@pytest.fixture
def heading_block(block_data, block_text_data):
    def create_heading_data(block_type) -> dict:
        data = block_text_data
        data["is_toggleable"] = IS_TOGGLEABLE
        return block_data(block_type, data)

    return create_heading_data


def assert_heading_data_is_correct(data, expected_data):
    assert_block_data_is_correct(data, expected_data)
    block_type = data.__class__.get_associated_block_type()
    heading_data = getattr(data, f"{block_type.value}")
    heading_expected_data = expected_data[block_type.value]

    assert_rich_text_structure(heading_data.rich_text, heading_expected_data["rich_text"])
    assert heading_data.color == heading_expected_data["color"]
    assert heading_data.is_toggleable == heading_expected_data["is_toggleable"]


@pytest.mark.parametrize("heading_class", [Heading1, Heading2, Heading3])
def test_heading_structure(heading_block, heading_class):
    extract_create_assert_structure(heading_block, heading_class, assert_heading_data_is_correct)


@pytest.mark.parametrize("heading_class", [Heading1, Heading2, Heading3])
def test_heading_serialization(heading_block, heading_class):
    extract_create_assert_serialization(heading_block, heading_class)
