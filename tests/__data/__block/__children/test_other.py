from uuid import UUID

import pytest

from __block.helper import extract_create_assert_structure, extract_create_assert_serialization
from notion_api.data.blocks import Callout, SyncedBlock
from __block.assertions import assert_block_data_is_correct
from __data.utils.__structures import create_rich_text_data, create_emoji_data, assert_rich_text_structure, \
    assert_icon_structure

# Constants
TEST_CONTENT = "Test content"
COLOR = "yellow"
EMOJI = create_emoji_data("💡")
BLOCK_ID = UUID("123e4567-e89b-12d3-a456-426614174000")
CALLOUT_DATA = {
    "rich_text": [
        create_rich_text_data(TEST_CONTENT, COLOR)
    ],
    "icon": EMOJI,
    "color": COLOR,
}

SYNCED_BLOCK_DATA = {
    "synced_from": {"block_id": BLOCK_ID},
    "children": [],
}


@pytest.fixture
def callout_block(block_data):
    def create_callout_data(block_type) -> dict:
        return block_data(block_type, CALLOUT_DATA)

    return create_callout_data


@pytest.fixture
def synced_block(block_data):
    def create_synced_block_data(block_type) -> dict:
        return block_data(block_type, SYNCED_BLOCK_DATA)

    return create_synced_block_data


def assert_callout_data_is_correct(data: Callout, expected_data: dict):
    assert_block_data_is_correct(data, expected_data)
    callout_data = data.callout
    expected_callout_data = expected_data["callout"]
    assert_rich_text_structure(callout_data.rich_text, expected_callout_data["rich_text"])
    assert_icon_structure(callout_data.icon, expected_callout_data["icon"])
    assert callout_data.color == expected_callout_data["color"]


def assert_synced_block_data_is_correct(data: SyncedBlock, expected_data: dict):
    assert_block_data_is_correct(data, expected_data)
    synced_block_data = data.synced_block
    expected_synced_block_data = expected_data["synced_block"]

    if synced_block_data.synced_from is not None:
        assert synced_block_data.synced_from.block_id == expected_synced_block_data["synced_from"]["block_id"]
    assert synced_block_data.children == expected_synced_block_data["children"]


@pytest.mark.parametrize(
    "block_class, fixture_name, assert_func", [
        (Callout, "callout_block", assert_callout_data_is_correct),
        (SyncedBlock, "synced_block", assert_synced_block_data_is_correct),
    ])
def test_block_structure(request, block_class, fixture_name, assert_func):
    extract_create_assert_structure(request.getfixturevalue(fixture_name), block_class, assert_func)


@pytest.mark.parametrize(
    "block_class, fixture_name", [
        (Callout, "callout_block"),
        (SyncedBlock, "synced_block"),
    ])
def test_block_serialization(request, block_class, fixture_name):
    extract_create_assert_serialization(request.getfixturevalue(fixture_name), block_class)
