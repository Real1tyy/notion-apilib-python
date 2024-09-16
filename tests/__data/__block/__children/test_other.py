# Standard Library
from uuid import UUID

# Third Party
import pytest

# First Party
from notion_apilib.data.blocks import Callout, SyncedBlock
from tests.__data.__block.assertions import assert_block_data_is_correct
from tests.__data.__block.helper import (
    extract_create_assert_serialization,
    extract_create_assert_structure,
)
from tests.__data.__structures.assertions import (
    assert_icon_structure,
    assert_rich_text_structure,
)
from tests.__data.__structures.conftest import create_emoji

BLOCK_ID = UUID("123e4567-e89b-12d3-a456-426614174000")


@pytest.fixture
def callout_block(block_data, block_text_data, create_emoji):
    def create_callout_data(block_type) -> dict:
        data = block_text_data
        data["icon"] = create_emoji
        return block_data(block_type, data)

    return create_callout_data


@pytest.fixture
def synced_block(block_data):
    def create_synced_block_data(block_type) -> dict:
        SYNCED_BLOCK_DATA = {
            "synced_from": {"block_id": BLOCK_ID},
            "children": [],
        }
        return block_data(block_type, SYNCED_BLOCK_DATA)

    return create_synced_block_data


def assert_callout_data_is_correct(data: Callout, expected_data: dict):
    assert_block_data_is_correct(data, expected_data)
    callout_data = data.callout
    expected_callout_data = expected_data["callout"]
    assert_rich_text_structure(
        callout_data.rich_text, expected_callout_data["rich_text"]
    )
    assert_icon_structure(callout_data.icon, expected_callout_data["icon"])
    assert callout_data.color == expected_callout_data["color"]


def assert_synced_block_data_is_correct(data: SyncedBlock, expected_data: dict):
    assert_block_data_is_correct(data, expected_data)
    synced_block_data = data.synced_block
    expected_synced_block_data = expected_data["synced_block"]

    if synced_block_data.synced_from is not None:
        assert (
                synced_block_data.synced_from.block_id
                == expected_synced_block_data["synced_from"]["block_id"]
        )
    assert synced_block_data.children == expected_synced_block_data["children"]


@pytest.mark.parametrize(
    "block_fixture, block_class, assert_func",
    [
        ("callout_block", Callout, assert_callout_data_is_correct),
        ("synced_block", SyncedBlock, assert_synced_block_data_is_correct),
    ],
)
def test_block_structure(request, block_fixture, block_class, assert_func):
    block_data = request.getfixturevalue(block_fixture)
    extract_create_assert_structure(block_data, block_class, assert_func)


@pytest.mark.parametrize(
    "block_fixture, block_class",
    [
        ("callout_block", Callout),
        ("synced_block", SyncedBlock),
    ],
)
def test_block_serialization(request, block_fixture, block_class):
    block_data = request.getfixturevalue(block_fixture)
    extract_create_assert_serialization(block_data, block_class)
