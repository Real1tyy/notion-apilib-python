import pytest

from notion_api.data.blocks import (
    BulletedListItem,
    NumberedListItem,
    Paragraph,
    Quote,
    ToDo,
    Toggle,
    BlockType,
)
from __data.block import add_block_data, assert_block_data_is_correct, create_block_structure
from __data.utils import create_rich_text_data, assert_rich_text_data

TEST_CONTENT = "Test content"
COLOR = "blue"


def _create_item_data(block_type) -> dict:
    @add_block_data(block_type)
    def item_data():
        return {
            "rich_text": [
                create_rich_text_data(TEST_CONTENT, COLOR)
            ],
            "color": COLOR,
            "children": [],
        }

    return item_data()


def _create_todo_data(block_type) -> dict:
    def todo_data() -> dict:
        base_data = _create_item_data(BlockType.TO_DO)
        base_data["to_do"]["checked"] = True
        return base_data

    return todo_data()


@pytest.fixture
def item_block():
    return _create_item_data


@pytest.fixture
def todo_block():
    return _create_todo_data


@pytest.mark.parametrize("item_class", [BulletedListItem, NumberedListItem, Paragraph, Quote, Toggle])
def test_item_structure(item_block, item_class):
    item = create_block_structure(item_class, item_block)
    assert_item_data_correct(item)


def test_todo_structure(todo_block):
    item = create_block_structure(ToDo, todo_block)
    assert_todo_data_correct(item)


def assert_item_data_correct(data):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    item_data = getattr(data, f"{block_type.value}")

    assert len(item_data.rich_text) == 1
    rich_text = item_data.rich_text[0]

    assert_rich_text_data(rich_text, TEST_CONTENT, COLOR)
    assert item_data.color == COLOR
    assert item_data.children == []


def assert_todo_data_correct(data: ToDo):
    assert_item_data_correct(data)
    block_type = data.__class__.get_associated_block_type()
    todo_data = getattr(data, f"{block_type.value}")
    assert todo_data.checked is True
