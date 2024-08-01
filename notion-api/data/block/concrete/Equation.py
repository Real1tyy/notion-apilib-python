from pydantic import BaseModel

from Block import Block


class EquationAttributes(BaseModel):
    expression: str


class Equation(Block):
    equation: EquationAttributes
