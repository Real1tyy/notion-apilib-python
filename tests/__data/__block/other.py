import pytest

from notion_api.data.blocks import Divider, ColumnList, Breadcrumb, Unsupported, Block
from __data.block import add_block_data, assert_block_data_is_correct, create_block_structure


def _create_empty_block_data(block_type) -> dict:
    @add_block_data(block_type)
    def empty_data():
        return {}

    return empty_data()


@pytest.fixture
def empty_block():
    return _create_empty_block_data


@pytest.mark.parametrize("block_class", [Divider, ColumnList, Breadcrumb, Unsupported])
def test_empty_block_structure(empty_block, block_class):
    item = create_block_structure(block_class, empty_block)
    assert_empty_block_data_correct(item)


def assert_empty_block_data_correct(data: Block):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    # No additional assertions are necessary as these blocks have no specific attributes
