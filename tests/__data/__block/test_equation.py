# Third Party
import pytest

# First Party
from notion_apilib.data.blocks import Equation
from tests.__data.__block.assertions import assert_block_data_is_correct
from tests.__data.__block.helper import extract_create_assert_serialization, extract_create_assert_structure

# Constants
EQUATION_EXPRESSION = "E = mc^2"


@pytest.fixture
def equation_block(block_data):
    def create_equation_data(block_type) -> dict:
        EQUATION_DATA = {
            "expression": EQUATION_EXPRESSION,
        }
        return block_data(block_type, EQUATION_DATA)

    return create_equation_data


def assert_equation_data_is_correct(data: Equation, expected_data: dict):
    assert_block_data_is_correct(data, expected_data)
    equation_data = data.equation
    expected_equation_data = expected_data["equation"]

    # Verify the expression
    assert equation_data.expression == expected_equation_data["expression"]


def test_block_structure(equation_block):
    extract_create_assert_structure(equation_block, Equation, assert_equation_data_is_correct)


def test_block_serialization(equation_block):
    extract_create_assert_serialization(equation_block, Equation)
