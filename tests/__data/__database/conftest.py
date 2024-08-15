import pytest

from notion_api.data import Page
from ..__properties.conftest import property_data
from ..__properties.test_date import date_database, DateDatabase
from ..__properties.test_number import unique_id_database, number_database, NumberDatabase, UniqueIdDatabase
from .constants import *


@pytest.fixture
def database_properties(date_database, unique_id_database, number_database):
    date_data = date_database(DateDatabase.get_associated_property_type())
    unique_id_data = unique_id_database(UniqueIdDatabase.get_associated_property_type())
    number_data = number_database(NumberDatabase.get_associated_property_type())
    return {
        date_data["name"]: date_data,
        unique_id_data["name"]: unique_id_data,
        number_data["name"]: number_data,
    }


@pytest.fixture
def create_database(major_object_data, database_properties):
    data = major_object_data('database')
    data["title"] = DATABASE_TITLE
    data["description"] = DATABASE_DESCRIPTION
    data["is_inline"] = False
    data["properties"] = database_properties
    return data


@pytest.fixture
def database_object(create_database):
    return Page(**create_database)
