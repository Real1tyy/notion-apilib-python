import pytest

from tests.__data.__structures.assertions import assert_user_structure
from .helper import extract_create_assert_structure, extract_create_assert_serialization
from .assertions import assert_properties_data_is_correct
from notion_api.data.properties import CreatedByPage, CreatedByDatabase, LastEditedByPage, LastEditedByDatabase, \
    PeoplePage, PeopleDatabase


@pytest.fixture
def created_by_page(property_data, create_user_data):
    def create_created_by_page(property_type):
        return property_data(property_type, create_user_data)

    return create_created_by_page


@pytest.fixture
def created_by_database(property_data):
    def create_created_by_database(property_type):
        return property_data(property_type, {})

    return create_created_by_database


@pytest.fixture
def last_edited_by_page(property_data, create_user_data):
    def create_last_edited_by_page(property_type):
        return property_data(property_type, create_user_data)

    return create_last_edited_by_page


@pytest.fixture
def last_edited_by_database(property_data):
    def create_last_edited_by_database(property_type):
        return property_data(property_type, {})

    return create_last_edited_by_database


@pytest.fixture
def people_page(property_data, create_user_data):
    def create_people_page(property_type):
        return property_data(property_type, [create_user_data])

    return create_people_page


@pytest.fixture
def people_database(property_data):
    def create_people_database(property_type):
        return property_data(property_type, {})

    return create_people_database


def assert_created_by_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert_user_structure(data.created_by, expected_data["created_by"])


def assert_created_by_database_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.created_by == expected_data["created_by"]


def assert_last_edited_by_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert_user_structure(data.last_edited_by, expected_data["last_edited_by"])


def assert_last_edited_by_database_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.last_edited_by == expected_data["last_edited_by"]


def assert_people_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    people = data.people
    expected_people = expected_data["people"]
    for person, expected_person in zip(people, expected_people):
        assert_user_structure(person, expected_person)


def assert_people_database_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.people == expected_data["people"]


@pytest.mark.parametrize(
    "property_fixture, property_class, assert_func", [
        ("created_by_page", CreatedByPage, assert_created_by_page_is_correct),
        ("created_by_database", CreatedByDatabase, assert_created_by_database_is_correct),
        ("last_edited_by_page", LastEditedByPage, assert_last_edited_by_page_is_correct),
        ("last_edited_by_database", LastEditedByDatabase, assert_last_edited_by_database_is_correct),
        ("people_page", PeoplePage, assert_people_page_is_correct),
        ("people_database", PeopleDatabase, assert_people_database_is_correct),
    ]
)
def test_property_structure(request, property_fixture, property_class, assert_func):
    extract_create_assert_structure(request.getfixturevalue(property_fixture), property_class, assert_func)


@pytest.mark.parametrize(
    "property_fixture, property_class", [
        ("created_by_page", CreatedByPage),
        ("created_by_database", CreatedByDatabase),
        ("last_edited_by_page", LastEditedByPage),
        ("last_edited_by_database", LastEditedByDatabase),
        ("people_page", PeoplePage),
        ("people_database", PeopleDatabase),
    ]
)
def test_property_serialization(request, property_fixture, property_class):
    extract_create_assert_serialization(request.getfixturevalue(property_fixture), property_class)
