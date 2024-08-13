import pytest

from ..helper import extract_create_assert_structure, extract_create_assert_serialization
from ...__block.assertions import assert_block_data_is_correct
from notion_api.data.blocks import BulletedListItem, NumberedListItem, Paragraph, Quote, Toggle, ToDo, BlockType
from __structures.assertions import assert_rich_text_structure
from ...__structures.conftest import create_rich_text

# Constants
IS_CHECKED = True


@pytest.fixture
def item_block(block_data, block_text_data):
    def create_item_data(block_type) -> dict:
        data = block_text_data
        data["children"] = []
        return block_data(block_type, data)

    return create_item_data


@pytest.fixture
def todo_block(block_data, item_block):
    def create_todo_data() -> dict:
        data = item_block(BlockType.TO_DO)
        data["to_do"]["checked"] = IS_CHECKED
        return data

    return lambda block_type: create_todo_data()


def assert_item_data_is_correct(data, expected_data):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, expected_data)
    item_data = getattr(data, f"{block_type.value}")
    expected_item_data = expected_data[block_type.value]

    assert_rich_text_structure(item_data.rich_text, expected_item_data["rich_text"])
    assert item_data.color == expected_item_data["color"]
    assert item_data.children == expected_item_data["children"]


def assert_todo_data_is_correct(data: ToDo, expected_data):
    assert_item_data_is_correct(data, expected_data)
    todo_data = getattr(data, f"{BlockType.TO_DO.value}")
    assert todo_data.checked == expected_data["to_do"]["checked"]


@pytest.mark.parametrize("block_class", [BulletedListItem, NumberedListItem, Paragraph, Quote, Toggle])
def test_item_block_structure(block_class, item_block):
    extract_create_assert_structure(item_block, block_class, assert_item_data_is_correct)


@pytest.mark.parametrize("block_class", [ToDo])
def test_todo_block_structure(block_class, todo_block):
    extract_create_assert_structure(todo_block, block_class, assert_todo_data_is_correct)


@pytest.mark.parametrize("block_class", [BulletedListItem, NumberedListItem, Paragraph, Quote, Toggle])
def test_item_block_serialization(block_class, item_block):
    extract_create_assert_serialization(item_block, block_class)


@pytest.mark.parametrize("block_class", [ToDo, ])
def test_todo_block_serialization(block_class, todo_block):
    extract_create_assert_serialization(todo_block, block_class)
