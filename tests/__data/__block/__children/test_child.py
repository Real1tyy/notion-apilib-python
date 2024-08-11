import pytest

from ....__data.block import add_block_data, assert_block_data_is_correct, create_block_structure
from notion_api.data.blocks import ChildPage, ChildDatabase

TITLE = "BEST TITLE"


@pytest.fixture
def child_block():
    def _create_child_data(block_type) -> dict:
        @add_block_data(block_type)
        def child_data():
            return {
                "title": TITLE,
            }

        return child_data()

    return _create_child_data


@pytest.mark.parametrize("child_class", [ChildPage, ChildDatabase])
def test_child_structure(child_block, child_class):
    child = create_block_structure(child_class, child_block)
    assert_child_data_is_correct(child)


def assert_child_data_is_correct(data):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    child_data = getattr(data, f"{block_type.value}")
    assert child_data.title == TITLE
