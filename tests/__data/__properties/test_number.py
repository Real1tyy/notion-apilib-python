# Third Party
import pytest

# First Party
from notion_apilib.data.properties import NumberDatabase, NumberPage, UniqueIdDatabase, UniqueIdPage

from .assertions import assert_properties_data_is_correct
from .helper import extract_create_assert_serialization, extract_create_assert_structure

# Constants for Number Properties
NUMBER_VALUE = 123.45
NUMBER_FORMAT = "currency"

# Constants for Unique ID Properties
UNIQUE_ID_NUMBER = 98765.4321
UNIQUE_ID_PREFIX_OPTIONS = ["ID-", None]


@pytest.fixture
def number_page(property_data):
    def create_number_page(property_type):
        return property_data(property_type, NUMBER_VALUE)

    return create_number_page


@pytest.fixture
def number_database(property_data):
    def create_number_database(property_type):
        NUMBER_DATABASE_DATA = {
            "format": NUMBER_FORMAT,
        }
        return property_data(property_type, NUMBER_DATABASE_DATA)

    return create_number_database


@pytest.fixture(params=UNIQUE_ID_PREFIX_OPTIONS)
def unique_id_page(request, property_data):
    def create_unique_id_page(property_type):
        UNIQUE_ID_PAGE_DATA = {
            "number": UNIQUE_ID_NUMBER,
            "prefix": request.param,
        }
        return property_data(property_type, UNIQUE_ID_PAGE_DATA)

    return create_unique_id_page


@pytest.fixture(params=UNIQUE_ID_PREFIX_OPTIONS)
def unique_id_database(request, property_data):
    def create_unique_id_database(property_type):
        UNIQUE_ID_DATABASE_DATA = {
            "prefix": request.param,
        }
        return property_data(property_type, UNIQUE_ID_DATABASE_DATA)

    return create_unique_id_database


def assert_number_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.number == expected_data["number"]


def assert_number_database_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    expected_data = expected_data["number"]
    assert data.number.format == expected_data["format"]


def assert_unique_id_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    expected_data = expected_data["unique_id"]
    assert data.unique_id.number == expected_data["number"]
    assert data.unique_id.prefix == expected_data["prefix"]


def assert_unique_id_database_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    expected_data = expected_data["unique_id"]
    assert data.unique_id.prefix == expected_data["prefix"]


@pytest.mark.parametrize(
    "property_fixture, property_class, assert_func", [
        ("number_page", NumberPage, assert_number_page_is_correct),
        ("number_database", NumberDatabase, assert_number_database_is_correct),
    ]
)
def test_number_property_structure(request, property_fixture, property_class, assert_func):
    extract_create_assert_structure(request.getfixturevalue(property_fixture), property_class, assert_func)


def test_unique_id_page_structure(unique_id_page):
    extract_create_assert_structure(unique_id_page, UniqueIdPage, assert_unique_id_page_is_correct)


def test_unique_id_page_serialization(unique_id_page):
    extract_create_assert_serialization(unique_id_page, UniqueIdPage)


@pytest.mark.parametrize(
    "property_fixture, property_class", [
        ("number_page", NumberPage),
        ("number_database", NumberDatabase),
    ]
)
def test_number_property_serialization(request, property_fixture, property_class):
    extract_create_assert_serialization(request.getfixturevalue(property_fixture), property_class)


def test_unique_id_database_structure(unique_id_database):
    extract_create_assert_structure(unique_id_database, UniqueIdDatabase, assert_unique_id_database_is_correct)


def test_unique_id_database_serialization(unique_id_database):
    extract_create_assert_serialization(unique_id_database, UniqueIdDatabase)
