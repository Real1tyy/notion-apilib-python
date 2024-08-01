from pydantic import BaseModel

from Block import Block, _create_block_object
from BlockType import BlockType
from Parent import Parent


class EquationAttributes(BaseModel):
    expression: str


class Equation(Block):
    equation: EquationAttributes


def create_equation_object(parent: Parent, expression: str) -> Equation:
    """
    Factory method to create Equation object
    :param parent: parent object
    :param expression: expression for the equation
    :return: newly created Equation Object
    """
    return _create_block_object(
        Equation,
        parent=parent,
        block_type=BlockType.EQUATION,
        equation=EquationAttributes(expression=expression)
    )