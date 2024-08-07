from _blocks.data import Equation, EquationAttributes
from _blocks._factory.general import _create_block
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
        block_type_specific_params=EquationAttributes(expression=expression)
    )


__all__ = [
    'create_equation'
]
