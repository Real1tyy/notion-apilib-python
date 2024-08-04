# Third Party
from Block import Block, _create_block
from BlockType import BlockType
from Parent import Parent
from pydantic import BaseModel


class EquationAttributes(BaseModel):
    expression: str


class Equation(Block):
    equation: EquationAttributes


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
