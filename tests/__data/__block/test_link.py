# Third Party
import pytest

# First Party
from notion_apilib.data.blocks import Bookmark, LinkPreview
from tests.__data.__block.assertions import assert_block_data_is_correct
from tests.__data.__block.helper import extract_create_assert_serialization, extract_create_assert_structure
from tests.__data.__structures.assertions import assert_rich_text_structure
from tests.__data.__structures.conftest import create_rich_text

# Constants
BOOKMARK_URL = "https://example.com/bookmark"
LINK_URL = "https://example.com/embed"


@pytest.fixture
def bookmark_block(block_data, create_rich_text):
    def create_bookmark_data(block_type) -> dict:
        BOOKMARK_DATA = {
            "url": BOOKMARK_URL,
            "caption": create_rich_text,
        }
        return block_data(block_type, BOOKMARK_DATA)

    return create_bookmark_data


@pytest.fixture
def link_block(block_data):
    def create_link_data(block_type) -> dict:
        LINK_DATA = {
            "url": LINK_URL,
        }
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
    "block_fixture, block_class, assert_func", [
        ("bookmark_block", Bookmark, assert_bookmark_data_is_correct),
        ("link_block", LinkPreview, assert_embed_or_link_preview_data_is_correct),
    ]
)
def test_block_structure(request, block_fixture, block_class, assert_func):
    block_data = request.getfixturevalue(block_fixture)
    extract_create_assert_structure(block_data, block_class, assert_func)


@pytest.mark.parametrize(
    "block_fixture, block_class", [
        ("bookmark_block", Bookmark),
        ("link_block", LinkPreview),
    ]
)
def test_block_serialization(request, block_fixture, block_class):
    block_data = request.getfixturevalue(block_fixture)
    extract_create_assert_serialization(block_data, block_class)
