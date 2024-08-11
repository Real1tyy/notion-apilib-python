import pytest

from __data.block import add_block_data, assert_block_data_is_correct, create_block_structure
from notion_api.data.blocks import Heading1, Heading2, Heading3, BlockType
from __data.utils import create_rich_text_data, assert_rich_text_data


@pytest.fixture
def heading_block():
    def _create_heading_data(block_type) -> dict:
        @add_block_data(block_type)
        def heading_data():
            return {
                "rich_text": [
                    create_rich_text_data("Lacinato kale", "green")
                ],
                "color": "green",
                "is_toggleable": False
            }

        return heading_data()

    return _create_heading_data


@pytest.mark.parametrize("heading_class", [Heading1, Heading2, Heading3])
def test_heading_structure(heading_block, heading_class):
    heading = create_block_structure(heading_class, heading_block)
    assert_heading_data_correct(heading)


def assert_heading_data_correct(data):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    heading_data = getattr(data, f"{block_type.value}")

    assert len(heading_data.rich_text) == 1
    rich_text = heading_data.rich_text[0]

    assert_rich_text_data(rich_text, "Lacinato kale", "green")

    # Verify other heading attributes
    assert heading_data.color == "green"
    assert heading_data.is_toggleable is False
