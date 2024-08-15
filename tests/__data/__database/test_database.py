import pytest

from notion_api.data import Page
from .assertions import assert_database_structure
from notion_api.data.properties import DateDatabase


def test_page(create_database):
    database_data = create_database.copy()
    database_data["properties"] = create_database["properties"].copy()
    page = Page(**database_data)
    assert_database_structure(page, create_database)


def test_page_properties(database_object, date_database):
    amount = len(database_object.get_properties())
    property_ = DateDatabase(**date_database(DateDatabase.get_associated_property_type()))
    database_object.add_property(property_)
    assert amount + 1 == len(database_object.get_properties())
