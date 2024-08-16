# Third Party
import pytest

# First Party
from notion_api.data import Page
from notion_api.data.properties import DatePage

from .assertions import assert_page_structure


def test_page(create_page):
    page_data = create_page.copy()
    page_data["properties"] = create_page["properties"].copy()
    page = Page(**page_data)
    assert_page_structure(page, create_page)


def test_page_properties(page_object, date_page):
    amount = len(page_object.properties())
    property_ = DatePage(**date_page(DatePage.get_associated_property_type()))
    page_object.add_property(property_)
    assert amount + 1 == len(page_object.properties())
