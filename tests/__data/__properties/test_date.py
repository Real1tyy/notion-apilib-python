# Standard Library
from datetime import datetime, timezone

# Third Party
import pytest

# First Party
from notion_apilib.data.properties import DateDatabase, DatePage

from .assertions import assert_properties_data_is_correct
from .helper import extract_create_assert_serialization, extract_create_assert_structure

START = datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
END_OPTIONS = [datetime(2021, 1, 1, 0, 0, 0, tzinfo=timezone.utc), None]
TIME_ZONE_OPTIONS = ["America/New_York", None]


@pytest.fixture(params=[(end, tz) for end in END_OPTIONS for tz in TIME_ZONE_OPTIONS])
def date_page(request, property_data):
    def create_page_database(property_type):
        end, time_zone = request.param
        PAGE_DATA = {
            "end": end,
            "start": START,
            "time_zone": time_zone,
        }
        return property_data(property_type, PAGE_DATA)

    return create_page_database


@pytest.fixture
def date_database(property_data):
    def create_date_database(property_type):
        return property_data(property_type, {})

    return create_date_database


def assert_date_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    expected_date_data = expected_data["date"]
    assert data.date.end == expected_date_data["end"]
    assert data.date.start == expected_date_data["start"]
    assert data.date.time_zone == expected_date_data["time_zone"]


def assert_date_database_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.date == expected_data["date"]


def test_date_database_structure(date_database):
    extract_create_assert_structure(date_database, DateDatabase, assert_date_database_is_correct)


def test_date_page_structure(date_page):
    extract_create_assert_structure(date_page, DatePage, assert_date_page_is_correct)


def test_date_database_serialization(date_database):
    extract_create_assert_serialization(date_database, DateDatabase)


def test_date_page_serialization(date_page):
    extract_create_assert_serialization(date_page, DatePage)
