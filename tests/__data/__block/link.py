import pytest

from notion_api.data.blocks import Bookmark, Embed, LinkPreview, BlockType
from __data.block import add_block_data, assert_block_data_is_correct, create_block_structure
from __data.utils import create_rich_text_data, assert_rich_text_data

# Constants
BOOKMARK_URL = "https://example.com/bookmark"
LINK_URL = "https://example.com/embed"
BOOKMARK_CAPTION_CONTENT = "Bookmark Caption"
CAPTION_COLOR = "blue"


def _create_bookmark_data(block_type) -> dict:
    @add_block_data(block_type)
    def bookmark_data():
        return {
            "url": BOOKMARK_URL,
            "caption": [
                create_rich_text_data(BOOKMARK_CAPTION_CONTENT, CAPTION_COLOR)
            ],
        }

    return bookmark_data()


def _create_link_data(block_type) -> dict:
    @add_block_data(block_type)
    def link_data():
        return {
            "url": LINK_URL,
        }

    return link_data()


@pytest.fixture
def bookmark_block():
    return _create_bookmark_data


@pytest.fixture
def link_block():
    return _create_link_data


def test_bookmark_structure(bookmark_block):
    item = create_block_structure(Bookmark, bookmark_block)
    assert_bookmark_data_correct(item)


@pytest.mark.parametrize("block_class", [Embed, LinkPreview])
def test_embed_and_link_preview_structure(link_block, block_class):
    item = create_block_structure(block_class, link_block)
    assert_embed_or_link_preview_data_correct(item)


def assert_bookmark_data_correct(data: Bookmark):
    block_type = Bookmark.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    bookmark_data = data.bookmark

    # Verify the URL
    assert bookmark_data.url == BOOKMARK_URL

    # Verify the caption
    assert len(bookmark_data.caption) == 1
    caption = bookmark_data.caption[0]
    assert_rich_text_data(caption, BOOKMARK_CAPTION_CONTENT, CAPTION_COLOR)


def assert_embed_or_link_preview_data_correct(data):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    link_data = getattr(data, f"{block_type.value}")
    assert link_data.url == LINK_URL
