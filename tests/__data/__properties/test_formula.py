# Third Party
import pytest

# First Party
from notion_apilib.data.properties import FormulaDatabase, FormulaPage

from .assertions import assert_properties_data_is_correct
from .helper import extract_create_assert_serialization, extract_create_assert_structure

# Constants for Formula Properties
FORMULA_TYPE = "number"
FORMULA_NUMBER = 123.45
FORMULA_BOOLEAN = None
FORMULA_DATE = None
FORMULA_STRING = None
FORMULA_EXPRESSION = "2 + 2"


@pytest.fixture
def formula_page(property_data):
    def create_formula_page(property_type):
        FORMULA_PAGE_DATA = {
            "type": FORMULA_TYPE,
            "number": FORMULA_NUMBER,
            "boolean": FORMULA_BOOLEAN,
            "date": FORMULA_DATE,
            "string": FORMULA_STRING,
        }
        return property_data(property_type, FORMULA_PAGE_DATA)

    return create_formula_page


@pytest.fixture
def formula_database(property_data):
    def create_formula_database(property_type):
        FORMULA_DATABASE_DATA = {
            "expression": FORMULA_EXPRESSION,
        }
        return property_data(property_type, FORMULA_DATABASE_DATA)

    return create_formula_database


def assert_formula_page_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    expected_data = expected_data["formula"]
    assert data.formula.type == expected_data["type"]
    assert data.formula.number == expected_data["number"]
    assert data.formula.boolean == expected_data["boolean"]
    assert data.formula.date == expected_data["date"]
    assert data.formula.string == expected_data["string"]


def assert_formula_database_is_correct(data, expected_data):
    assert_properties_data_is_correct(data, expected_data)
    expected_data = expected_data["formula"]
    assert data.formula.expression == expected_data["expression"]


@pytest.mark.parametrize(
    "property_fixture, property_class, assert_func",
    [
        ("formula_database", FormulaDatabase, assert_formula_database_is_correct),
        ("formula_page", FormulaPage, assert_formula_page_is_correct),
    ],
)
def test_formula_structure(request, property_fixture, property_class, assert_func):
    extract_create_assert_structure(
        request.getfixturevalue(property_fixture), property_class, assert_func
    )


@pytest.mark.parametrize(
    "property_fixture, property_class",
    [
        ("formula_database", FormulaDatabase),
        ("formula_page", FormulaPage),
    ],
)
def test_formula_serialization(request, property_fixture, property_class):
    extract_create_assert_serialization(
        request.getfixturevalue(property_fixture), property_class
    )
