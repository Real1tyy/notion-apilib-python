# Standard Library
from typing import Optional

# First Party
from notion_api.data._properties._data.number import (
    NumberDatabase,
    NumberPage,
    NumberStructure,
    UniqueIdDatabase,
    UniqueIdPage,
    UniqueIdPageStructure,
)

from .general import _create_database_property, _create_page_property


def create_number_page(
        parent: 'Page', name: str, number: float) -> NumberPage:
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
        name=name,
        property_specific_params=number
    )


def create_number_database(
        parent: 'Database', name: str, format_: str) -> NumberDatabase:
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
        name=name,
        property_specific_params=NumberStructure(format=format_)
    )


def create_unique_id_page(
        parent: 'Page', name: str, number: float, prefix: Optional[str] = None) -> UniqueIdPage:
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
        name=name,
        property_specific_params=UniqueIdPageStructure(number=number, prefix=prefix)
    )


def create_unique_id_database(
        parent: 'Database', name: str) -> UniqueIdDatabase:
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
        name=name,
        property_specific_params={}
    )


__all__ = ['create_number_page', 'create_number_database', 'create_unique_id_page', 'create_unique_id_database']
