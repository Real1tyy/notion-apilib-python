# Third Party
import pytest

# First Party
import notion_apilib.data as notion
from notion_apilib.data.properties import DateDatabase

from .assertions import assert_database_structure


def test_database(create_database):
    database_data = create_database.copy()
    database_data["properties"] = create_database["properties"].copy()
    database = notion.Database(**database_data)
    assert_database_structure(database, create_database)


def test_database_properties(database_object, date_database):
    amount = len(database_object.properties())
    property_ = DateDatabase(**date_database(DateDatabase.get_associated_property_type()))
    database_object.add_property(property_)
    assert amount + 1 == len(database_object.properties())
