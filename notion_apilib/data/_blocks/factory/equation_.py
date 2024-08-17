# First Party
from notion_apilib.data.structures import Parent

from ..data import Equation, block_structures
from ._general import _create_block


def create_equation(parent: Parent, expression: str) -> Equation:
    """
    Factory method to create Equation object
    :param parent: parent object
    :param expression: expression for the equation
    :return: newly created Equation Object
    """
    return _create_block(
        Equation,
        parent=parent,
        block_type_specific_params=block_structures.EquationAttributes(
            expression=expression
        ),
    )


__all__ = ["create_equation"]
