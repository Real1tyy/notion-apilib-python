import pytest

from notion_api.data.blocks import Bookmark, Embed, LinkPreview
from __block.helper import extract_create_assert_structure, extract_create_assert_serialization
from __block.assertions import assert_block_data_is_correct
from __data.utils.__structures import create_rich_text_data, assert_rich_text_structure

# Constants
BOOKMARK_URL = "https://example.com/bookmark"
LINK_URL = "https://example.com/embed"
BOOKMARK_CAPTION_CONTENT = "Bookmark Caption"
CAPTION_COLOR = "blue"

BOOKMARK_DATA = {
    "url": BOOKMARK_URL,
    "caption": [
        create_rich_text_data(BOOKMARK_CAPTION_CONTENT, CAPTION_COLOR)
    ],
}

LINK_DATA = {
    "url": LINK_URL,
}


@pytest.fixture
def bookmark_block(block_data):
    def create_bookmark_data(block_type) -> dict:
        return block_data(block_type, BOOKMARK_DATA)

    return create_bookmark_data


@pytest.fixture
def link_block(block_data):
    def create_link_data(block_type) -> dict:
        return block_data(block_type, LINK_DATA)

    return create_link_data


def assert_bookmark_data_is_correct(data: Bookmark, expected_data: dict):
    assert_block_data_is_correct(data, expected_data)
    bookmark_data = data.bookmark
    expected_bookmark_data = expected_data["bookmark"]

    assert bookmark_data.url == expected_bookmark_data["url"]
    assert_rich_text_structure(bookmark_data.caption, expected_bookmark_data["caption"])


def assert_embed_or_link_preview_data_is_correct(data, expected_data: dict):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, expected_data)
    link_data = getattr(data, f"{block_type.value}")
    assert link_data.url == expected_data[block_type.value]["url"]


@pytest.mark.parametrize(
    "block_class, fixture_name, assert_func", [
        (Bookmark, "bookmark_block", assert_bookmark_data_is_correct),
        (LinkPreview, "link_block", assert_embed_or_link_preview_data_is_correct)
    ])
def test_block_structure(request, block_class, fixture_name, assert_func):
    extract_create_assert_structure(request.getfixturevalue(fixture_name), block_class, assert_func)


@pytest.mark.parametrize(
    "block_class, fixture_name", [
        (Bookmark, "bookmark_block"),
        (LinkPreview, "link_block")
    ])
def test_block_serialization(request, block_class, fixture_name):
    extract_create_assert_serialization(request.getfixturevalue(fixture_name), block_class)
