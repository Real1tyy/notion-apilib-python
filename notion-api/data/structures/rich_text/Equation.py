from pydantic import BaseModel


class Equation(BaseModel):
    expression: str
