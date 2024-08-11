import pytest

from notion_api.data.blocks import Equation
from __data.block import add_block_data, assert_block_data_is_correct, create_block_structure

# Constants
EQUATION_EXPRESSION = "E = mc^2"


def _create_equation_data(block_type) -> dict:
    @add_block_data(block_type)
    def equation_data():
        return {
            "expression": EQUATION_EXPRESSION,
        }

    return equation_data()


@pytest.fixture
def equation_block():
    return _create_equation_data


def test_equation_structure(equation_block):
    item = create_block_structure(Equation, equation_block)
    assert_equation_data_correct(item)


def assert_equation_data_correct(data: Equation):
    block_type = Equation.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)
    equation_data = data.equation

    # Verify the expression
    assert equation_data.expression == EQUATION_EXPRESSION
