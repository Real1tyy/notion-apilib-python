# Standard Library
from typing import Any, Optional

from pydantic import BaseModel

# Third Party
from property import DatabaseProperty, PageProperty


class NumberPage(PageProperty):
    """
    A model representing a number property for a page.

    Attributes:
        number (float): The number value of the page property.
    """
    number: float


class NumberStructure(BaseModel):
    """
    A model representing the structure for a number property in a database.

    Attributes:
        format (str): The format of the number.
    """
    format: str


class NumberDatabase(DatabaseProperty):
    """
    A model representing a number property for a database.

    Attributes:
        number (NumberStructure): The structure of the number property.
    """
    number: NumberStructure


class UniqueIdStructure(BaseModel):
    """
    A model representing the structure for a unique ID property.

    Attributes:
        number (float): The number value of the unique ID.
        prefix (Optional[str]): The optional prefix of the unique ID.
    """
    number: float
    prefix: Optional[str] = None


class UniqueIdPage(PageProperty):
    """
    A model representing a unique ID property for a page.

    Attributes:
        unique_id (UniqueIdStructure): The unique ID structure of the page property.
    """
    unique_id: UniqueIdStructure


class UniqueIdDatabase(DatabaseProperty):
    """
    A model representing a unique ID property for a database.

    Attributes:
        unique_id (dict[str, Any]): The dictionary representing the unique ID property for the database.
    """
    unique_id: dict[str, Any]
