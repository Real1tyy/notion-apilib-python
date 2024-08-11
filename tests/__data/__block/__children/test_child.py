import pytest

from __block.assertions import assert_block_data_is_correct, create_block_structure, assert_serialization_to_json
from notion_api.data.blocks import ChildPage, ChildDatabase

TITLE = "BEST TITLE"
CHILD_DATA = {
    "title": TITLE,
}


@pytest.fixture
def child_block(block_data):
    def create_child_data(block_type) -> dict:
        data = block_data(block_type, CHILD_DATA)
        return data

    return create_child_data


@pytest.mark.parametrize("child_class", [ChildPage, ChildDatabase])
def test_child_structure(child_block, child_class):
    child = create_block_structure(child_class, child_block)
    assert_child_data_is_correct(child)


@pytest.mark.parametrize("child_class", [ChildPage, ChildDatabase])
def test_child_serialization(child_block, child_class):
    child = create_block_structure(child_class, child_block)
    assert_serialization_to_json(child, CHILD_DATA)


def assert_child_data_is_correct(data):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    child_data = getattr(data, f"{block_type.value}")
    assert child_data.title == TITLE
