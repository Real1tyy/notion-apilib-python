import pytest

from notion_api.data.blocks import Divider, ColumnList, Breadcrumb, Unsupported, Block
from __block.assertions import assert_block_data_is_correct, create_block_structure


@pytest.fixture
def empty_block(block_data):
    def create_empty_data(block_type) -> dict:
        empty_data = {}
        data = block_data(block_type, empty_data)
        return data

    return create_empty_data


@pytest.mark.parametrize("block_class", [Divider, ColumnList, Breadcrumb, Unsupported])
def test_empty_block_structure(empty_block, block_class):
    item = create_block_structure(block_class, empty_block)
    assert_empty_block_data_is_correct(item)


def assert_empty_block_data_is_correct(data: Block):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
