# Standard Library
from typing import Callable
from uuid import UUID

# Third Party
import pytest

# First Party
from notion_api.data.properties import (
    CheckboxDatabase,
    CheckboxPage,
    MultiSelectDatabase,
    MultiSelectPage,
    SelectDatabase,
    SelectPage,
    StatusDatabase,
    StatusPage,
)

from ..utils.__serialization import transform_dictionary
from .assertions import (
    assert_properties_data_is_correct,
    create_property_object,
    extract_property_data,
)
from .helper import extract_create_assert_serialization, extract_create_assert_structure

# Constants for Checkbox Properties
CHECKBOX_VALUE = True

# Constants for Select and Multi-Select Options
OPTION_NAME = "Option 1"
OPTION_COLOR = "blue"
OPTION_ID = "c02fc1d3-db8b-45c5-a222-27595b15aea7"

GROUP_OPTION_IDS = [
    "c02fc1d3-db8b-45c5-a222-27595b15aea7",
    "c02fc1d3-db8b-45c5-a222-27595b15aea7",
]

# Constants for Status Properties
STATUS_OPTION_NAME = "In Progress"
STATUS_GROUP_OPTION_IDS = ["id1", "id2", "id3"]


@pytest.fixture
def create_option():
    return {
        "id": OPTION_ID,
        "name": OPTION_NAME,
        "color": OPTION_COLOR,
    }


@pytest.fixture
def create_group(create_option):
    data = create_option.copy()
    data["option_ids"] = GROUP_OPTION_IDS
    return data


@pytest.fixture
def create_options(create_option):
    return [create_option, create_option.copy()]


@pytest.fixture
def create_groups(create_group):
    return [create_group, create_group.copy()]


@pytest.fixture
def checkbox_page(property_data):
    def create_checkbox_page(property_type):
        return property_data(property_type, CHECKBOX_VALUE)

    return create_checkbox_page


@pytest.fixture
def checkbox_database(property_data):
    def create_checkbox_database(property_type):
        return property_data(property_type, {})

    return create_checkbox_database


@pytest.fixture
def multi_select_page(property_data, create_options):
    def create_multi_select_page(property_type):
        MULTI_SELECT_PAGE_DATA = {
            "options": create_options,
        }
        return property_data(property_type, MULTI_SELECT_PAGE_DATA)

    return create_multi_select_page


@pytest.fixture
def multi_select_database(property_data, create_options):
    def create_multi_select_database(property_type):
        MULTI_SELECT_DATABASE_DATA = {
            "options": create_options,
        }
        return property_data(property_type, MULTI_SELECT_DATABASE_DATA)

    return create_multi_select_database


@pytest.fixture
def select_page(property_data, create_option):
    def create_select_page(property_type):
        return property_data(property_type, create_option)

    return create_select_page


@pytest.fixture
def select_database(property_data, create_options):
    def create_select_database(property_type):
        SELECT_DATABASE_DATA = {
            "options": create_options,
        }
        return property_data(property_type, SELECT_DATABASE_DATA)

    return create_select_database


@pytest.fixture
def status_page(property_data, create_option):
    def create_status_page(property_type):
        return property_data(property_type, create_option)

    return create_status_page


@pytest.fixture
def status_database(property_data, create_groups, create_options):
    def create_status_database(property_type):
        STATUS_DATABASE_DATA = {
            "options": create_options,
            "groups": create_groups,
        }
        return property_data(property_type, STATUS_DATABASE_DATA)

    return create_status_database


def assert_checkbox_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert data.checkbox == expected_data["checkbox"]


def assert_checkbox_database_is_correct(data, expected_data):
    assert_checkbox_page_is_correct(data, expected_data)


def assert_option_structure_is_correct(options, expected_options):
    for option, expected_option in zip(options, expected_options):
        assert option.name == expected_option["name"]
        assert option.color == expected_option["color"]
        assert option.id == expected_option["id"]


def assert_group_structure_is_correct(groups, expected_groups):
    for group, expected_group in zip(groups, expected_groups):
        assert group.name == expected_group["name"]
        assert group.color == expected_group["color"]
        assert group.id == expected_group["id"]
        assert group.option_ids == expected_group["option_ids"]


def assert_multi_select_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert_option_structure_is_correct(
        data.multi_select.options, expected_data["multi_select"]["options"]
    )


def assert_multi_select_database_is_correct(data, expected_data):
    assert_multi_select_page_is_correct(data, expected_data)


def assert_select_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert_option_structure_is_correct([data.select], [expected_data["select"]])


def assert_select_database_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert_option_structure_is_correct(
        data.select.options, expected_data["select"]["options"]
    )


def assert_status_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert_option_structure_is_correct([data.status], [expected_data["status"]])


def assert_status_database_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    assert_option_structure_is_correct(
        data.status.options, expected_data["status"]["options"]
    )
    assert_group_structure_is_correct(
        data.status.groups, expected_data["status"]["groups"]
    )


def transform_page_option(option: dict) -> dict:
    option.pop("id")
    option.pop("color")
    return option


def transform_database_option(option: dict) -> dict:
    option.pop("id")
    return option


def transform_options_groups_data(data, change_function: Callable):
    if not isinstance(data, dict):
        return
    data = transform_dictionary(data)
    for key, value in data.items():
        if key == "options" or key == "groups":
            options = []
            for option in value:
                options.append(change_function(option))
            data[key] = options
    if "id" in data and "color" in data:
        return change_function(data)
    return data


@pytest.mark.parametrize(
    "property_fixture, property_class, assert_func",
    [
        ("checkbox_page", CheckboxPage, assert_checkbox_page_is_correct),
        ("checkbox_database", CheckboxDatabase, assert_checkbox_database_is_correct),
        ("multi_select_page", MultiSelectPage, assert_multi_select_page_is_correct),
        (
            "multi_select_database",
            MultiSelectDatabase,
            assert_multi_select_database_is_correct,
        ),
        ("select_page", SelectPage, assert_select_page_is_correct),
        ("select_database", SelectDatabase, assert_select_database_is_correct),
        ("status_page", StatusPage, assert_status_page_is_correct),
        ("status_database", StatusDatabase, assert_status_database_is_correct),
    ],
)
def test_property_structure(request, property_fixture, property_class, assert_func):
    extract_create_assert_structure(
        request.getfixturevalue(property_fixture), property_class, assert_func
    )


def serialization_options_tester(data_provider, property_class, transform_option):
    data = extract_property_data(data_provider, property_class)
    property_ = create_property_object(data, property_class)
    json = property_.serialize_to_json()
    property_data = transform_options_groups_data(
        data[property_class.get_payload_property_name()], transform_option
    )
    assert json[property_class.get_payload_property_name()] == property_data


@pytest.mark.parametrize(
    "property_fixture, property_class",
    [
        ("multi_select_page", MultiSelectPage),
        ("select_page", SelectPage),
        ("status_page", StatusPage),
    ],
)
def test_page_serialization(request, property_fixture, property_class):
    serialization_options_tester(
        request.getfixturevalue(property_fixture), property_class, transform_page_option
    )


@pytest.mark.parametrize(
    "property_fixture, property_class",
    [
        ("multi_select_database", MultiSelectDatabase),
        ("select_database", SelectDatabase),
        ("status_database", StatusDatabase),
    ],
)
def test_database_serialization(request, property_fixture, property_class):
    serialization_options_tester(
        request.getfixturevalue(property_fixture),
        property_class,
        transform_database_option,
    )


@pytest.mark.parametrize(
    "property_fixture, property_class",
    [
        ("checkbox_page", CheckboxPage),
        ("checkbox_database", CheckboxDatabase),
    ],
)
def test_checkbox_serialization(request, property_fixture, property_class):
    extract_create_assert_serialization(
        request.getfixturevalue(property_fixture), property_class
    )
