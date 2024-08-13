import pytest
from .constants import *

parent_types = ['page_id', 'workspace']


# parent_types = ['page_id', 'database_id', 'block_id', 'workspace']


@pytest.fixture(params=parent_types)
def parent_data(request):
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


# user_types = ['person', 'bot']
user_types = ['person']


@pytest.fixture(params=user_types)
def user_data(request):
    return {
        'object': 'user',
        "id": USER_ID,
        "type": request.param,
        "name": USER_NAME,
        "avatar_url": USER_AVATAR_URL,
    }


rich_text_type = ['text', 'mention', 'equation']


@pytest.fixture
def text():
    return {
        "content": RICH_TEXT_CONTENT,
        "link": {
            "url": TEXT_LINK,
        }
    }


@pytest.fixture
def equation():
    return {
        "expression": EQUATION_EXPRESSION,
    }


@pytest.fixture
def mention():
    return {
        "type": "user",
        "user": {
            "object": "user",
            "id": MENTION_USER_ID,
        }
    }


@pytest.fixture(params=rich_text_type)
def create_rich_text(request, text, equation, mention) -> list[dict]:
    basic_data = {
        "type": request.param,
        "annotations": {
            "bold": False,
            "italic": False,
            "strikethrough": False,
            "underline": False,
            "code": False,
            "color": RICH_TEXT_COLOR
        },
        "plain_text": RICH_TEXT_CONTENT,
        "href": None
    }
    match request.param:
        case "text":
            basic_data[request.param] = text
        case "mention":
            basic_data[request.param] = mention
        case "equation":
            basic_data[request.param] = equation
    return [basic_data]


@pytest.fixture
def create_emoji() -> dict:
    return {
        "type": "emoji",
        "emoji": EMOJI_EMOJI
    }
