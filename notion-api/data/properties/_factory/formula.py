from datetime import datetime
from typing import Literal, Optional

from FormulaProperty import FormulaPage, FormulaStructure
from Page import Page
from PropertyType import PropertyType
from factory.general import _create_page_property


def create_formula_page(
        parent: Page, name: str, type_: Literal['boolean', 'date', 'number', 'string'],
        number: Optional[float] = None, boolean: Optional[bool] = None,
        date: Optional[datetime] = None, string: Optional[str] = None,
        id_: Optional[str] = None) -> FormulaPage:
    """
    Factory method to create a FormulaPage object.

    Parameters:
        parent (Page): The parent page to which this formula property belongs.
        name (str): The name of the formula property.
        type_ (Literal['boolean', 'date', 'number', 'string']): The type of the formula.
        number (Optional[float]): The optional number value of the formula.
        boolean (Optional[bool]): The optional boolean value of the formula.
        date (Optional[datetime]): The optional date value of the formula.
        string (Optional[str]): The optional string value of the formula.
        id_ (Optional[str]): The optional ID of the formula property.

    Returns:
        FormulaPage: A new FormulaPage object.
    """
    return _create_page_property(
        FormulaPage,
        parent=parent,
        property_type=PropertyType.FORMULA,
        name=name,
        id_=id_,
        formula=FormulaStructure(type=type_, number=number, boolean=boolean, date=date, string=string)
    )
