import pytest

from notion_api.data.blocks import Bookmark, Embed, LinkPreview
from __block.assertions import assert_block_data_is_correct, create_block_structure
from __data.utils.__structures import create_rich_text_data, assert_rich_text_structure

# Constants
BOOKMARK_URL = "https://example.com/bookmark"
LINK_URL = "https://example.com/embed"
BOOKMARK_CAPTION_CONTENT = "Bookmark Caption"
CAPTION_COLOR = "blue"


@pytest.fixture
def bookmark_block(block_data):
    def create_bookmark_data(block_type) -> dict:
        bookmark_data = {
            "url": BOOKMARK_URL,
            "caption": [
                create_rich_text_data(BOOKMARK_CAPTION_CONTENT, CAPTION_COLOR)
            ],
        }
        data = block_data(block_type, bookmark_data)
        return data

    return create_bookmark_data


@pytest.fixture
def link_block(block_data):
    def create_link_data(block_type) -> dict:
        link_data = {
            "url": LINK_URL,
        }
        data = block_data(block_type, link_data)
        return data

    return create_link_data


def test_bookmark_structure(bookmark_block):
    bookmark = create_block_structure(Bookmark, bookmark_block)
    assert_bookmark_data_is_correct(bookmark)


@pytest.mark.parametrize("block_class", [Embed, LinkPreview])
def test_embed_and_link_preview_structure(link_block, block_class):
    item = create_block_structure(block_class, link_block)
    assert_embed_or_link_preview_data_is_correct(item)


def assert_bookmark_data_is_correct(data: Bookmark):
    block_type = Bookmark.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    bookmark_data = data.bookmark

    assert bookmark_data.url == BOOKMARK_URL
    assert_rich_text_structure(bookmark_data.caption, BOOKMARK_CAPTION_CONTENT, CAPTION_COLOR)


def assert_embed_or_link_preview_data_is_correct(data):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    link_data = getattr(data, f"{block_type.value}")
    assert link_data.url == LINK_URL
