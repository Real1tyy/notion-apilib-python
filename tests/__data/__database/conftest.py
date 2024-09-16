# Third Party
import pytest

# First Party
from notion_apilib.data import Database, Page

from ..__properties.conftest import property_data
from ..__properties.test_date import DateDatabase, date_database
from ..__properties.test_number import NumberDatabase, UniqueIdDatabase, number_database, unique_id_database
from ..__properties.test_text import TitleDatabase, title_database
from .constants import *


@pytest.fixture
def database_properties(date_database, unique_id_database, number_database, title_database):
    date_data = date_database(DateDatabase.get_associated_property_type())
    unique_id_data = unique_id_database(UniqueIdDatabase.get_associated_property_type())
    number_data = number_database(NumberDatabase.get_associated_property_type())
    title_data = title_database(TitleDatabase.get_associated_property_type())
    return {
        date_data["name"]: date_data,
        unique_id_data["name"]: unique_id_data,
        number_data["name"]: number_data,
        title_data["name"]: title_data,
    }


@pytest.fixture
def create_database(major_object_data, database_properties, create_rich_text):
    data = major_object_data("database")
    data["title"] = create_rich_text
    data["description"] = create_rich_text
    data["is_inline"] = False
    data["properties"] = database_properties
    return data


@pytest.fixture
def database_object(create_database):
    return Database(**create_database)
