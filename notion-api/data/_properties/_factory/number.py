from typing import Optional

from _properties.type_ import PropertyType
from database import Database
from general import _create_page_property, _create_database_property
from number import UniqueIdPage, UniqueIdStructure, NumberPage, UniqueIdDatabase, NumberDatabase, \
    NumberStructure
from page import Page


def create_number_page(
        parent: Page, name: str, number: float) -> NumberPage:
    """
    Factory method to create a NumberPage object.

    Parameters:
        parent (Page): The parent page to which this number property belongs.
        name (str): The name of the number property.
        number (float): The number value of the property.

    Returns:
        NumberPage: A new NumberPage object.
    """
    return _create_page_property(
        NumberPage,
        parent=parent,
        property_type=PropertyType.NUMBER,
        name=name,
        number=number
    )


def create_number_database(
        parent: Database, name: str, format_: str) -> NumberDatabase:
    """
    Factory method to create a NumberDatabase object.

    Parameters:
        parent (Database): The parent database to which this number property belongs.
        name (str): The name of the number property.
        format_ (str): The format of the number property.

    Returns:
        NumberDatabase: A new NumberDatabase object.
    """
    return _create_database_property(
        NumberDatabase,
        parent=parent,
        property_type=PropertyType.NUMBER,
        name=name,
        number=NumberStructure(format=format_)
    )


def create_unique_id_page(
        parent: Page, name: str, number: float, prefix: Optional[str] = None) -> UniqueIdPage:
    """
    Factory method to create a UniqueIdPage object.

    Parameters:
        parent (Page): The parent page to which this unique ID property belongs.
        name (str): The name of the unique ID property.
        number (float): The number value of the unique ID.
        prefix (Optional[str]): The optional prefix of the unique ID.

    Returns:
        UniqueIdPage: A new UniqueIdPage object.
    """
    return _create_page_property(
        UniqueIdPage,
        parent=parent,
        property_type=PropertyType.UNIQUE_ID,
        name=name,
        unique_id=UniqueIdStructure(number=number, prefix=prefix)
    )


def create_unique_id_database(
        parent: Database, name: str) -> UniqueIdDatabase:
    """
    Factory method to create a UniqueIdDatabase object.

    Parameters:
        parent (Database): The parent database to which this unique ID property belongs.
        name (str): The name of the unique ID property.

    Returns:
        UniqueIdDatabase: A new UniqueIdDatabase object.
    """
    return _create_database_property(
        UniqueIdDatabase,
        parent=parent,
        property_type=PropertyType.UNIQUE_ID,
        name=name,
        unique_id={}
    )
