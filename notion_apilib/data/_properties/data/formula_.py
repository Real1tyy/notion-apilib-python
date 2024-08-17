# Standard Library
from datetime import datetime
from typing import Literal, Optional

# Third Party
from pydantic import BaseModel

from ..property import DatabaseProperty, PageProperty
from ..type_ import PropertyType


class FormulaStructure(BaseModel):
    """
    A model representing a formula structure with a type and optional number, boolean, date, and string fields.

    Attributes:
        type (Literal['boolean', 'date', 'number', 'string']): The type of the formula.
        number (Optional[float]): The optional number value of the formula.
        boolean (Optional[bool]): The optional boolean value of the formula.
        date (Optional[datetime]): The optional date value of the formula.
        string (Optional[str]): The optional string value of the formula.
    """

    type: Literal["boolean", "date", "number", "string"]
    number: Optional[float] = None
    boolean: Optional[bool] = None
    date: Optional[datetime] = None
    string: Optional[str] = None


class FormulaPage(PageProperty):
    """
    A model representing a formula property for a page.

    Attributes:
        formula (FormulaStructure): The formula structure of the page property.
    """

    formula: FormulaStructure

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.FORMULA


class FormulaDatabaseStructure(BaseModel):
    """
    A model representing the structure for a formula property in a database.

    Attributes:
        expression (str): The expression of the formula.
    """

    expression: str


class FormulaDatabase(DatabaseProperty):
    """
    A model representing a formula property for a database.

    Attributes:
        formula (FormulaDatabaseStructure): The formula structure of the database property.
    """

    formula: FormulaDatabaseStructure

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.FORMULA


__all__ = ["FormulaDatabase", "FormulaPage"]
