# Third Party
from pydantic import BaseModel

from _blocks.block import Block


class EquationAttributes(BaseModel):
    """
    Attributes for an equation block.

    :param expression: The mathematical expression of the equation.
    :type expression: str
    """
    expression: str


class Equation(Block):
    """
    Represents an Equation block.

    :param equation: Attributes for the equation block.
    :type equation: EquationAttributes
    """
    equation: EquationAttributes
