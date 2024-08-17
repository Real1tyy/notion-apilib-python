# Third Party
import pytest

# First Party
from notion_apilib.data.blocks import BlockType, BulletedListItem, NumberedListItem, Paragraph, Quote, ToDo, Toggle
from tests.__data.__block.assertions import assert_block_data_is_correct
from tests.__data.__structures.assertions import assert_rich_text_structure

from ..helper import extract_create_assert_serialization, extract_create_assert_structure

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


@pytest.mark.parametrize(
    "block_fixture, block_class, assert_func", [
        ("item_block", BulletedListItem, assert_item_data_is_correct),
        ("item_block", NumberedListItem, assert_item_data_is_correct),
        ("item_block", Paragraph, assert_item_data_is_correct),
        ("item_block", Quote, assert_item_data_is_correct),
        ("item_block", Toggle, assert_item_data_is_correct),
        ("todo_block", ToDo, assert_todo_data_is_correct),
    ]
)
def test_block_structure(request, block_fixture, block_class, assert_func):
    block_data = request.getfixturevalue(block_fixture)
    extract_create_assert_structure(block_data, block_class, assert_func)


@pytest.mark.parametrize(
    "block_fixture, block_class", [
        ("item_block", BulletedListItem),
        ("item_block", NumberedListItem),
        ("item_block", Paragraph),
        ("item_block", Quote),
        ("item_block", Toggle),
        ("todo_block", ToDo),
    ]
)
def test_block_serialization(request, block_fixture, block_class):
    block_data = request.getfixturevalue(block_fixture)
    extract_create_assert_serialization(block_data, block_class)
