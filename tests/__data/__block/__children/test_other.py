from uuid import UUID

import pytest

from notion_api.data.blocks import Callout, SyncedBlock, Emoji
from __block.assertions import assert_block_data_is_correct, create_block_structure, assert_serialization_to_json
from __data.utils.__structures import create_rich_text_data, create_emoji_data, assert_rich_text_structure

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
        data = block_data(block_type, CALLOUT_DATA)
        return data

    return create_callout_data


@pytest.fixture
def synced_block(block_data):
    def create_synced_block_data(block_type) -> dict:
        data = block_data(block_type, SYNCED_BLOCK_DATA)
        return data

    return create_synced_block_data


def test_callout_structure(callout_block):
    callout = create_block_structure(Callout, callout_block)
    assert_callout_data_is_correct(callout)


def test_callout_serialization(callout_block):
    callout = create_block_structure(Callout, callout_block)
    assert_serialization_to_json(callout, CALLOUT_DATA)


def test_synced_block_structure(synced_block):
    synced_block_instance = create_block_structure(SyncedBlock, synced_block)
    assert_synced_block_data_is_correct(synced_block_instance)


def test_synced_block_serialization(synced_block):
    synced_block_instance = create_block_structure(SyncedBlock, synced_block)
    assert_serialization_to_json(synced_block_instance, SYNCED_BLOCK_DATA)


def assert_callout_data_is_correct(data: Callout):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    callout_data = data.callout

    assert_rich_text_structure(callout_data.rich_text, TEST_CONTENT, COLOR)
    assert callout_data.icon == Emoji(**EMOJI)
    assert callout_data.color == COLOR


def assert_synced_block_data_is_correct(data: SyncedBlock):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    synced_block_data = data.synced_block

    assert synced_block_data.synced_from.block_id == BLOCK_ID
    assert synced_block_data.children == []
