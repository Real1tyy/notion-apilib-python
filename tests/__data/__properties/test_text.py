# Third Party
import pytest

# First Party
from notion_api.data.properties import RichTextDatabase, RichTextPage, TitleDatabase, TitlePage
from tests.__data.__structures.assertions import assert_rich_text_structure

from .assertions import assert_properties_data_is_correct
from .helper import extract_create_assert_serialization, extract_create_assert_structure


@pytest.fixture
def rich_text_page(property_data, create_rich_text):
    def create_rich_text_page(property_type):
        return property_data(property_type, create_rich_text)

    return create_rich_text_page


@pytest.fixture
def rich_text_database(property_data):
    def create_rich_text_database(property_type):
        return property_data(property_type, {})

    return create_rich_text_database


@pytest.fixture
def title_page(property_data, create_rich_text):
    def create_title_page(property_type):
        return property_data(property_type, create_rich_text)

    return create_title_page


@pytest.fixture
def title_database(property_data):
    def create_title_database(property_type):
        return property_data(property_type, {})

    return create_title_database


def assert_rich_text_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert_rich_text_structure(data.rich_text, expected_data["rich_text"])


def assert_rich_text_database_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.rich_text == expected_data["rich_text"]


def assert_title_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert_rich_text_structure(data.title_structure_model, expected_data["title"])


def assert_title_database_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.title_structure_model == expected_data["title"]


@pytest.mark.parametrize(
    "property_fixture, property_class, assert_func", [
        ("rich_text_page", RichTextPage, assert_rich_text_page_is_correct),
        ("rich_text_database", RichTextDatabase, assert_rich_text_database_is_correct),
        ("title_page", TitlePage, assert_title_page_is_correct),
        ("title_database", TitleDatabase, assert_title_database_is_correct),
    ]
)
def test_property_structure(request, property_fixture, property_class, assert_func):
    extract_create_assert_structure(request.getfixturevalue(property_fixture), property_class, assert_func)


@pytest.mark.parametrize(
    "property_fixture, property_class", [
        ("rich_text_page", RichTextPage),
        ("rich_text_database", RichTextDatabase),
        ("title_page", TitlePage),
        ("title_database", TitleDatabase),
    ]
)
def test_property_serialization(request, property_fixture, property_class):
    extract_create_assert_serialization(request.getfixturevalue(property_fixture), property_class)
