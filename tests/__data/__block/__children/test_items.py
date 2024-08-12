import pytest

from ..helper import extract_create_assert_structure, extract_create_assert_serialization
from ...__block.assertions import assert_block_data_is_correct, create_block_object, assert_serialization_to_json
from notion_api.data.blocks import BulletedListItem, NumberedListItem, Paragraph, Quote, Toggle, ToDo, BlockType
from ....__data.utils.__structures import create_rich_text_data, assert_rich_text_structure

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
        return block_data(block_type, ITEM_DATA)

    return create_item_data


@pytest.fixture
def todo_block(block_data):
    def create_todo_data() -> dict:
        return block_data(BlockType.TO_DO, TODO_DATA)

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


@pytest.mark.parametrize(
    "block_class, fixture_name, assert_func", [
        (BulletedListItem, "item_block", assert_item_data_is_correct),
        (NumberedListItem, "item_block", assert_item_data_is_correct),
        (Paragraph, "item_block", assert_item_data_is_correct),
        (Quote, "item_block", assert_item_data_is_correct),
        (Toggle, "item_block", assert_item_data_is_correct),
        (ToDo, "todo_block", assert_todo_data_is_correct),
    ])
def test_block_structure(request, block_class, fixture_name, assert_func):
    extract_create_assert_structure(request.getfixturevalue(fixture_name), block_class, assert_func)


@pytest.mark.parametrize(
    "block_class, fixture_name", [
        (BulletedListItem, "item_block"),
        (NumberedListItem, "item_block"),
        (Paragraph, "item_block"),
        (Quote, "item_block"),
        (Toggle, "item_block"),
        (ToDo, "todo_block"),
    ])
def test_block_serialization(request, block_class, fixture_name):
    extract_create_assert_serialization(request.getfixturevalue(fixture_name), block_class)
