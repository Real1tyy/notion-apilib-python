from datetime import datetime
from typing import Literal, Optional

from database import Database
from formula import FormulaPage, FormulaStructure, FormulaDatabase, FormulaDatabaseStructure
from general import _create_page_property, _create_database_property
from page import Page
from properties.type import PropertyType


def create_formula_page(
        parent: Page, name: str, type_: Literal['boolean', 'date', 'number', 'string'],
        number: Optional[float] = None, boolean: Optional[bool] = None,
        date: Optional[datetime] = None, string: Optional[str] = None) -> FormulaPage:
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

    Returns:
        FormulaPage: A new FormulaPage object.
    """
    return _create_page_property(
        FormulaPage,
        parent=parent,
        property_type=PropertyType.FORMULA,
        name=name,
        formula=FormulaStructure(type=type_, number=number, boolean=boolean, date=date, string=string)
    )


def create_formula_database(
        parent: Database, name: str, expression: str) -> FormulaDatabase:
    """
    Factory method to create a FormulaDatabase object.

    Parameters:
        parent (Database): The parent database to which this formula property belongs.
        name (str): The name of the formula property.
        expression (str): The expression of the formula.

    Returns:
        FormulaDatabase: A new FormulaDatabase object.
    """
    return _create_database_property(
        FormulaDatabase,
        parent=parent,
        property_type=PropertyType.FORMULA,
        name=name,
        formula=FormulaDatabaseStructure(expression=expression)
    )
