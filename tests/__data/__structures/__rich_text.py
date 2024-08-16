# Third Party
import pytest

from .constants import *


@pytest.fixture
def create_text():
    return {
        "content": RICH_TEXT_CONTENT,
        "link": {
            "url": TEXT_LINK,
        }
    }


@pytest.fixture
def create_equation():
    return {
        "expression": EQUATION_EXPRESSION,
    }


@pytest.fixture
def create_mention():
    return {
        "type": "user",
        "user": {
            "object": "user",
            "id": MENTION_USER_ID,
        }
    }


@pytest.fixture
def create_database_mention():
    return {
        "id": PARENT_DATABASE_ID,
    }


@pytest.fixture(params=MENTION_DATE_END_OPTIONS)
def create_date_mention(request):
    return {
        "start": MENTION_DATE_START,
        "end": request.param,
    }


@pytest.fixture(params=MENTION_DATE_END_OPTIONS)
def create_link_preview_mention(request):
    return {
        "url": MENTION_LINK_PREVIEW,
    }


@pytest.fixture()
def create_page_mention(request):
    return {
        "id": MENTION_PAGE_ID,
    }


@pytest.fixture(params=TEMPLATE_MENTION_DATE_OPTIONS)
def create_template_mention_date(request):
    return {
        "type": "template_mention_date",
        "template_mention_date": request.param,
    }


@pytest.fixture(params=TEMPLATE_MENTION_USER_OPTIONS)
def create_template_mention_user(request):
    return {
        "type": "template_mention_user",
        "template_mention_user": request.param,
    }


@pytest.fixture(params=TEMPLATE_MENTION_OPTIONS)
def create_template_mention(request, create_template_mention_date, create_template_mention_user):
    match request.param:
        case "template_mention_date":
            return create_template_mention_date
        case "template_mention_user":
            return create_template_mention_user


@pytest.fixture()
def create_user_mention(request):
    return {
        "object": "user",
        "id": MENTION_USER_ID,
    }


@pytest.fixture(params=MENTION_TYPES)
def create_extensive_mention(
        request, create_database_mention, create_date_mention, create_link_preview_mention,
        create_page_mention, create_template_mention, create_user_mention) -> dict:
    basic_data = {
        "type": request.param,
    }
    match request.param:
        case "database":
            basic_data[request.param] = create_database_mention
        case "date":
            basic_data[request.param] = create_date_mention
        case "link_preview":
            basic_data[request.param] = create_link_preview_mention
        case "page":
            basic_data[request.param] = create_page_mention
        case "template_mention":
            basic_data[request.param] = create_template_mention
        case "user":
            basic_data[request.param] = create_user_mention
    return basic_data


@pytest.fixture()
def create_rich_text(create_text) -> list[dict]:
    return [{
        "type": "text",
        "annotations": {
            "bold": False,
            "italic": False,
            "strikethrough": False,
            "underline": False,
            "code": False,
            "color": RICH_TEXT_COLOR
        },
        "plain_text": RICH_TEXT_CONTENT,
        "href": RICH_TEXT_URL,
        "text": create_text,
    }]


@pytest.fixture(params=RICH_TEXT_TYPE)
def create_extensive_rich_text(
        request, create_text, create_equation, create_extensive_mention, create_href) -> list[dict]:
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
        "href": create_href,
    }
    match request.param:
        case "text":
            basic_data[request.param] = create_text
        case "mention":
            basic_data[request.param] = create_extensive_mention
        case "equation":
            basic_data[request.param] = create_equation
    return [basic_data]
