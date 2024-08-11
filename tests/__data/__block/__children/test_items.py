import pytest

from __block.assertions import assert_block_data_is_correct, create_block_structure, assert_serialization_to_json
from notion_api.data.blocks import BulletedListItem, NumberedListItem, Paragraph, Quote, ToDo, Toggle, BlockType
from __data.utils.__structures import create_rich_text_data, assert_rich_text_structure

# Constants
TEST_CONTENT = "Test content"
COLOR = "blue"
IS_CHECKED = True
ITEM_DATA = {
    "rich_text": [
        create_rich_text_data(TEST_CONTENT, COLOR)
    ],
    "color": COLOR,
    "children": [],
}
TODO_DATA = {
    **ITEM_DATA,
    "checked": IS_CHECKED
}


@pytest.fixture
def item_block(block_data):
    def create_item_data(block_type) -> dict:
        data = block_data(block_type, ITEM_DATA)
        return data

    return create_item_data


@pytest.fixture
def todo_block(block_data):
    def create_todo_data() -> dict:
        data = block_data(BlockType.TO_DO, TODO_DATA)
        return data

    return lambda block_type: create_todo_data()


@pytest.mark.parametrize("item_class", [BulletedListItem, NumberedListItem, Paragraph, Quote, Toggle])
def test_item_structure(item_block, item_class):
    item = create_block_structure(item_class, item_block)
    assert_item_data_is_correct(item)


@pytest.mark.parametrize("item_class", [BulletedListItem, NumberedListItem, Paragraph, Quote, Toggle])
def test_item_serialization(item_block, item_class):
    item = create_block_structure(item_class, item_block)
    assert_serialization_to_json(item, ITEM_DATA)


def test_todo_structure(todo_block):
    todo = create_block_structure(ToDo, todo_block)
    assert_todo_data_is_correct(todo)


def test_todo_serialization(todo_block):
    todo = create_block_structure(ToDo, todo_block)
    assert_serialization_to_json(todo, TODO_DATA)


def assert_item_data_is_correct(data):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    item_data = getattr(data, f"{block_type.value}")

    assert_rich_text_structure(item_data.rich_text, TEST_CONTENT, COLOR)
    assert item_data.color == COLOR
    assert item_data.children == []


def assert_todo_data_is_correct(data: ToDo):
    assert_item_data_is_correct(data)
    todo_data = getattr(data, f"{BlockType.TO_DO.value}")
    assert todo_data.checked == IS_CHECKED
