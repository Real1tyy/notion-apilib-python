# Third Party
from pydantic import BaseModel

from ..block import Block, BlockType


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

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.EQUATION


__all__ = ["Equation"]
