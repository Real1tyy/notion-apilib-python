# Standard Library
from datetime import datetime, timezone
from uuid import UUID

# Third Party
import pytest

# First Party
from notion_apilib.data.properties import (
    RelationDatabase,
    RelationPage,
    RollupDatabase,
    RollupPage,
)

from .assertions import assert_properties_data_is_correct
from .constants import *
from .helper import extract_create_assert_serialization, extract_create_assert_structure

# Constants for Relation Properties
RELATED_ITEM_ID = UUID("123e4567-e89b-12d3-a456-426614174000")
RELATED_DATABASE_ID = UUID("123e4567-e89b-12d3-a456-426614174001")
SYNCED_PROPERTY_ID = "synced_property_id"
SYNCED_PROPERTY_NAME = "Synced Property Name"

# Constants for Rollup Properties
ROLLUP_FUNCTION = "count"
ROLLUP_TYPE = "number"
ROLLUP_NUMBER = 42.0
RELATED_PROPERTY_ID = "related_property_id"
RELATED_PROPERTY_NAME = "Related Property Name"
ROLLUP_PROPERTY_NAME = "Rollup Property Name"
ROLLUP_PROPERTY_ID = "rollup_property_id"
ROLLUP_DATE = datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)


@pytest.fixture
def relation_page(property_data):
    def create_relation_page(property_type):
        return {
            "id": PROPERTY_ID,
            "type": property_type,
            "name": PROPERTY_NAME,
            "relation": [{"id": RELATED_ITEM_ID}],
            "has_more": False,
        }

    return create_relation_page


@pytest.fixture
def relation_database(property_data):
    def create_relation_database(property_type):
        RELATION_DATABASE_DATA = {
            "database_id": RELATED_DATABASE_ID,
            "type": "dual_property",
            "dual_property": {
                "synced_property_id": SYNCED_PROPERTY_ID,
                "synced_property_name": SYNCED_PROPERTY_NAME,
            },
        }
        return property_data(property_type, RELATION_DATABASE_DATA)

    return create_relation_database


ROLLUP_TYPES = ["number", "array", "date", "incomplete", "unsupported"]


@pytest.fixture(params=ROLLUP_TYPES)
def rollup_page(request, property_data):
    def create_rollup_page(property_type):
        ROLLUP_PAGE_DATA = {
            "type": request.param,
            "function": ROLLUP_FUNCTION,
        }
        match request.param:
            case "number":
                ROLLUP_PAGE_DATA["number"] = ROLLUP_NUMBER
            case "array":
                ROLLUP_PAGE_DATA["array"] = [ROLLUP_NUMBER]
            case "date":
                ROLLUP_PAGE_DATA["date"] = ROLLUP_DATE
            case "incomplete":
                ROLLUP_PAGE_DATA["incomplete"] = None
            case "unsupported":
                ROLLUP_PAGE_DATA["unsupported"] = None

        return property_data(property_type, ROLLUP_PAGE_DATA)

    return create_rollup_page


@pytest.fixture
def rollup_database(property_data):
    def create_rollup_database(property_type):
        ROLLUP_DATABASE_DATA = {
            "relation_property_id": RELATED_PROPERTY_ID,
            "relation_property_name": RELATED_PROPERTY_NAME,
            "rollup_property_name": ROLLUP_PROPERTY_NAME,
            "rollup_property_id": ROLLUP_PROPERTY_ID,
            "function": ROLLUP_FUNCTION,
        }
        return property_data(property_type, ROLLUP_DATABASE_DATA)

    return create_rollup_database


def assert_relation_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.relation[0].id == expected_data["relation"][0]["id"]


def assert_relation_database_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.relation.database_id == expected_data["relation"]["database_id"]
    assert data.relation.type == expected_data["relation"]["type"]
    assert (
        data.relation.dual_property.synced_property_id
        == expected_data["relation"]["dual_property"]["synced_property_id"]
    )
    assert (
        data.relation.dual_property.synced_property_name
        == expected_data["relation"]["dual_property"]["synced_property_name"]
    )


def assert_rollup_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.rollup.type == expected_data["rollup"]["type"]
    match data.rollup.type:
        case "number":
            assert data.rollup.number == expected_data["rollup"]["number"]
        case "array":
            assert data.rollup.array == expected_data["rollup"]["array"]
        case "date":
            assert data.rollup.date == expected_data["rollup"]["date"]
        case "incomplete":
            assert data.rollup.incomplete == expected_data["rollup"]["incomplete"]
        case "unsupported":
            assert data.rollup.unsupported == expected_data["rollup"]["unsupported"]


def assert_rollup_database_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert (
        data.rollup.relation_property_id
        == expected_data["rollup"]["relation_property_id"]
    )
    assert (
        data.rollup.relation_property_name
        == expected_data["rollup"]["relation_property_name"]
    )
    assert (
        data.rollup.rollup_property_name
        == expected_data["rollup"]["rollup_property_name"]
    )
    assert (
        data.rollup.rollup_property_id == expected_data["rollup"]["rollup_property_id"]
    )
    assert data.rollup.function == expected_data["rollup"]["function"]


@pytest.mark.parametrize(
    "property_fixture, property_class, assert_func",
    [
        ("relation_page", RelationPage, assert_relation_page_is_correct),
        ("relation_database", RelationDatabase, assert_relation_database_is_correct),
        ("rollup_database", RollupDatabase, assert_rollup_database_is_correct),
    ],
)
def test_property_structure(request, property_fixture, property_class, assert_func):
    extract_create_assert_structure(
        request.getfixturevalue(property_fixture), property_class, assert_func
    )


def test_rollup_page_structure(rollup_page):
    extract_create_assert_structure(
        rollup_page, RollupPage, assert_rollup_page_is_correct
    )


@pytest.mark.parametrize(
    "property_fixture, property_class",
    [
        ("relation_page", RelationPage),
        ("relation_database", RelationDatabase),
        ("rollup_database", RollupDatabase),
    ],
)
def test_property_serialization(request, property_fixture, property_class):
    extract_create_assert_serialization(
        request.getfixturevalue(property_fixture), property_class
    )


def test_rollup_page_serialization(rollup_page):
    extract_create_assert_serialization(rollup_page, RollupPage)
