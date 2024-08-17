# Third Party
import pytest

# First Party
from notion_apilib.data import Page

from ..__properties.conftest import property_data
from ..__properties.test_date import DatePage, date_page
from ..__properties.test_number import NumberPage, UniqueIdPage, number_page, unique_id_page
from ..__properties.test_text import TitlePage, title_page


@pytest.fixture
def page_properties(date_page, unique_id_page, number_page, title_page):
    date_data = date_page(DatePage.get_associated_property_type())
    unique_id_data = unique_id_page(UniqueIdPage.get_associated_property_type())
    number_data = number_page(NumberPage.get_associated_property_type())
    title_data = title_page(TitlePage.get_associated_property_type())
    return {
        date_data["name"]: date_data,
        unique_id_data["name"]: unique_id_data,
        number_data["name"]: number_data,
        title_data["name"]: title_data,
    }


@pytest.fixture
def create_page(major_object_data, page_properties):
    data = major_object_data('page')
    data["properties"] = page_properties
    return data


@pytest.fixture
def page_object(create_page):
    return Page(**create_page)
