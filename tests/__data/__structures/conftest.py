# Third Party
import pytest

from .__rich_text import (
    create_equation,
    create_extensive_mention,
    create_mention,
    create_rich_text,
    create_template_mention,
    create_template_mention_date,
    create_template_mention_user,
    create_text,
    create_user_mention,
    create_page_mention,
    create_link_preview_mention,
    create_date_mention,
    create_database_mention,
    create_extensive_rich_text
)
from .constants import *


@pytest.fixture(params=HREF_OPTIONS)
def create_href(request):
    return request.param


@pytest.fixture()
def create_parent_data(request):
    return {
        "type": "page_id",
        "page_id": PARENT_PAGE_ID,
    }


@pytest.fixture(params=PARENT_TYPES)
def create_extensive_parent_data(request):
    basic_data = {
        "type": request.param,
    }
    match request.param:
        case "page_id":
            basic_data["page_id"] = PARENT_PAGE_ID
        case "database_id":
            basic_data["database_id"] = PARENT_DATABASE_ID
        case "block_id":
            basic_data["block_id"] = PARENT_BLOCK_ID
        case "workspace":
            basic_data["workspace"] = True
    return basic_data


@pytest.fixture()
def create_user_data(request):
    return {
        'object': 'user',
        "id": USER_ID,
        "type": "person",
        "name": USER_NAME,
        "avatar_url": USER_AVATAR_URL,
    }


@pytest.fixture(params=USER_TYPES)
def create_extensive_user_data(request, create_href):
    return {
        'object': 'user',
        "id": USER_ID,
        "type": request.param,
        "name": USER_NAME,
        "avatar_url": create_href,
    }


@pytest.fixture
def create_emoji() -> dict:
    return {
        "type": "emoji",
        "emoji": EMOJI_EMOJI
    }


@pytest.fixture
def create_file_object():
    return {
        "url": ICON_URL,
        "expiry_time": ICON_EXPIRY_TIME,
    }


@pytest.fixture
def create_external():
    return {
        "url": ICON_URL,
    }


@pytest.fixture()
def create_resource() -> dict:
    return {
        "type": "external",
        "external": {
            "url": ICON_URL,
        }
    }


@pytest.fixture(params=RESOURCE_TYPE)
def create_extensive_resource(request, create_file_object, create_external) -> dict:
    basic_data = {
        "type": request.param,
    }
    match request.param:
        case "external":
            basic_data[request.param] = create_external
        case "file":
            basic_data[request.param] = create_file_object
    return basic_data
