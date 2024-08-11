import pytest
from uuid import UUID

from notion_api.data.blocks import Callout, SyncedBlock, Emoji
from __data.block import add_block_data, assert_block_data_is_correct, create_block_structure
from __data.utils import create_rich_text_data, create_emoji_data, assert_rich_text_data

# Constants
TEST_CONTENT = "Test content"
COLOR = "yellow"
EMOJI = create_emoji_data("💡")
BLOCK_ID = UUID("123e4567-e89b-12d3-a456-426614174000")


def _create_callout_data(block_type) -> dict:
    @add_block_data(block_type)
    def callout_data():
        return {
            "rich_text": [
                create_rich_text_data(TEST_CONTENT, COLOR)
            ],
            "icon": EMOJI,
            "color": COLOR,
        }

    return callout_data()


def _create_synced_block_data(block_type) -> dict:
    @add_block_data(block_type)
    def synced_block_data():
        return {
            "synced_from": {"block_id": BLOCK_ID},
            "children": [],
        }

    return synced_block_data()


@pytest.fixture
def callout_block():
    return _create_callout_data


@pytest.fixture
def synced_block():
    return _create_synced_block_data


def test_callout_structure(callout_block):
    item = create_block_structure(Callout, callout_block)
    assert_callout_data_correct(item)


def test_synced_block_structure(synced_block):
    item = create_block_structure(SyncedBlock, synced_block)
    assert_synced_block_data_correct(item)


def assert_callout_data_correct(data: Callout):
    block_type = Callout.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    callout_data = data.callout

    assert len(callout_data.rich_text) == 1
    rich_text = callout_data.rich_text[0]

    assert_rich_text_data(rich_text, TEST_CONTENT, COLOR)

    assert callout_data.icon == Emoji(**EMOJI)
    assert callout_data.color == COLOR


def assert_synced_block_data_correct(data: SyncedBlock):
    block_type = SyncedBlock.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    synced_block_data = data.synced_block

    assert synced_block_data.synced_from.block_id == BLOCK_ID
    assert synced_block_data.children == []
