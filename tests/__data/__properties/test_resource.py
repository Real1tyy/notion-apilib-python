# Third Party
import pytest

# First Party
from notion_api.data.properties import (
    EmailDatabase,
    EmailPage,
    FilesDatabase,
    FilesPage,
    PhoneNumberDatabase,
    PhoneNumberPage,
    UrlDatabase,
    UrlPage,
)
from tests.__data.__structures.assertions import assert_resources_structure

from .assertions import assert_properties_data_is_correct
from .helper import extract_create_assert_serialization, extract_create_assert_structure

# Constants for Email Properties
EMAIL_VALUE = "example@example.com"

# Constants for Phone Number Properties
PHONE_NUMBER_VALUE = "+1234567890"

# Constants for URL Properties
URL_VALUE = "https://example.com"


@pytest.fixture
def email_page(property_data):
    def create_email_page(property_type):
        return property_data(property_type, EMAIL_VALUE)

    return create_email_page


@pytest.fixture
def email_database(property_data):
    def create_email_database(property_type):
        return property_data(property_type, {})

    return create_email_database


@pytest.fixture
def files_page(property_data, create_resource):
    def create_files_page(property_type):
        return property_data(property_type, [create_resource])

    return create_files_page


@pytest.fixture
def files_database(property_data):
    def create_files_database(property_type):
        return property_data(property_type, {})

    return create_files_database


@pytest.fixture
def phone_number_page(property_data):
    def create_phone_number_page(property_type):
        return property_data(property_type, PHONE_NUMBER_VALUE)

    return create_phone_number_page


@pytest.fixture
def phone_number_database(property_data):
    def create_phone_number_database(property_type):
        return property_data(property_type, {})

    return create_phone_number_database


@pytest.fixture
def url_page(property_data):
    def create_url_page(property_type):
        return property_data(property_type, URL_VALUE)

    return create_url_page


@pytest.fixture
def url_database(property_data):
    def create_url_database(property_type):
        return property_data(property_type, {})

    return create_url_database


def assert_email_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.email == expected_data["email"]


def assert_email_database_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.email == expected_data["email"]


def assert_files_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    files = data.files
    expected_files = expected_data["files"]
    for file, expected_file in zip(files, expected_files):
        assert_resources_structure(file, expected_file)


def assert_files_database_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.files == expected_data["files"]


def assert_phone_number_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.phone_number == expected_data["phone_number"]


def assert_phone_number_database_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.phone_number == expected_data["phone_number"]


def assert_url_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.url == expected_data["url"]


def assert_url_database_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.url == expected_data["url"]


@pytest.mark.parametrize(
    "property_fixture, property_class, assert_func", [
        ("email_page", EmailPage, assert_email_page_is_correct),
        ("email_database", EmailDatabase, assert_email_database_is_correct),
        ("files_page", FilesPage, assert_files_page_is_correct),
        ("files_database", FilesDatabase, assert_files_database_is_correct),
        ("phone_number_page", PhoneNumberPage, assert_phone_number_page_is_correct),
        ("phone_number_database", PhoneNumberDatabase, assert_phone_number_database_is_correct),
        ("url_page", UrlPage, assert_url_page_is_correct),
        ("url_database", UrlDatabase, assert_url_database_is_correct),
    ]
)
def test_property_structure(request, property_fixture, property_class, assert_func):
    extract_create_assert_structure(request.getfixturevalue(property_fixture), property_class, assert_func)


@pytest.mark.parametrize(
    "property_fixture, property_class", [
        ("email_page", EmailPage),
        ("email_database", EmailDatabase),
        ("files_page", FilesPage),
        ("files_database", FilesDatabase),
        ("phone_number_page", PhoneNumberPage),
        ("phone_number_database", PhoneNumberDatabase),
        ("url_page", UrlPage),
        ("url_database", UrlDatabase),
    ]
)
def test_property_serialization(request, property_fixture, property_class):
    extract_create_assert_serialization(request.getfixturevalue(property_fixture), property_class)
