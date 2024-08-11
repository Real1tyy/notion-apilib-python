import pytest

from notion_api.data.blocks import Equation
from __block.assertions import assert_block_data_is_correct, create_block_structure

# Constants
EQUATION_EXPRESSION = "E = mc^2"


@pytest.fixture
def equation_block(block_data):
    def create_equation_data(block_type) -> dict:
        equation_data = {
            "expression": EQUATION_EXPRESSION,
        }
        data = block_data(block_type, equation_data)
        return data

    return create_equation_data


def test_equation_structure(equation_block):
    equation = create_block_structure(Equation, equation_block)
    assert_equation_data_is_correct(equation)


def assert_equation_data_is_correct(data: Equation):
    block_type = Equation.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    equation_data = data.equation

    # Verify the expression
    assert equation_data.expression == EQUATION_EXPRESSION
