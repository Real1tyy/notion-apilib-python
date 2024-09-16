# Standard Library
from datetime import datetime, timezone

# Third Party
import pytest

# First Party
from notion_apilib.data.properties import (
    CreatedTimeDatabase,
    CreatedTimePage,
    LastEditedTimeDatabase,
    LastEditedTimePage,
)

from .assertions import assert_properties_data_is_correct
from .helper import extract_create_assert_serialization, extract_create_assert_structure

# Constants for Created Time and Last Edited Time Properties
CREATED_TIME_VALUE = datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
LAST_EDITED_TIME_VALUE = datetime(2022, 1, 1, 12, 0, 0, tzinfo=timezone.utc)


@pytest.fixture
def created_time_page(property_data):
    def create_created_time_page(property_type):
        return property_data(property_type, CREATED_TIME_VALUE)

    return create_created_time_page


@pytest.fixture
def created_time_database(property_data):
    def create_created_time_database(property_type):
        return property_data(property_type, {})

    return create_created_time_database


@pytest.fixture
def last_edited_time_page(property_data):
    def create_last_edited_time_page(property_type):
        return property_data(property_type, LAST_EDITED_TIME_VALUE)

    return create_last_edited_time_page


@pytest.fixture
def last_edited_time_database(property_data):
    def create_last_edited_time_database(property_type):
        return property_data(property_type, {})

    return create_last_edited_time_database


def assert_created_time_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.created_time == expected_data["created_time"]


def assert_created_time_database_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.created_time == expected_data["created_time"]


def assert_last_edited_time_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.last_edited_time == expected_data["last_edited_time"]


def assert_last_edited_time_database_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.last_edited_time == expected_data["last_edited_time"]


@pytest.mark.parametrize(
    "property_fixture, property_class, assert_func",
    [
        ("created_time_page", CreatedTimePage, assert_created_time_page_is_correct),
        (
            "created_time_database",
            CreatedTimeDatabase,
            assert_created_time_database_is_correct,
        ),
        (
            "last_edited_time_page",
            LastEditedTimePage,
            assert_last_edited_time_page_is_correct,
        ),
        (
            "last_edited_time_database",
            LastEditedTimeDatabase,
            assert_last_edited_time_database_is_correct,
        ),
    ],
)
def test_property_structure(request, property_fixture, property_class, assert_func):
    extract_create_assert_structure(
        request.getfixturevalue(property_fixture), property_class, assert_func
    )


@pytest.mark.parametrize(
    "property_fixture, property_class",
    [
        ("created_time_page", CreatedTimePage),
        ("created_time_database", CreatedTimeDatabase),
        ("last_edited_time_page", LastEditedTimePage),
        ("last_edited_time_database", LastEditedTimeDatabase),
    ],
)
def test_property_serialization(request, property_fixture, property_class):
    extract_create_assert_serialization(
        request.getfixturevalue(property_fixture), property_class
    )
