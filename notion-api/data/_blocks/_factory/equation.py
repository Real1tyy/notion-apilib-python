from _blocks.data import Equation, EquationAttributes
from block import _create_block
from _blocks.type import BlockType
from structures import Parent


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
        block_type=BlockType.EQUATION,
        equation=EquationAttributes(expression=expression)
    )
