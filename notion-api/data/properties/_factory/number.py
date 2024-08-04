from typing import Optional

from NumberProperty import UniqueIdPage, UniqueIdStructure, NumberPage
from Page import Page
from PropertyType import PropertyType
from factory.general import _create_page_property


def create_number_page(
        parent: Page, name: str, number: float, id_: Optional[str] = None) -> NumberPage:
    """
    Factory method to create a NumberPage object.

    Parameters:
        parent (Page): The parent page to which this number property belongs.
        name (str): The name of the number property.
        number (float): The number value of the property.
        id_ (Optional[str]): The optional ID of the number property.

    Returns:
        NumberPage: A new NumberPage object.
    """
    return _create_page_property(
        NumberPage,
        parent=parent,
        property_type=PropertyType.NUMBER,
        name=name,
        id_=id_,
        number=number
    )


def create_unique_id_page(
        parent: Page, name: str, number: float, prefix: Optional[str] = None,
        id_: Optional[str] = None) -> UniqueIdPage:
    """
    Factory method to create a UniqueIdPage object.

    Parameters:
        parent (Page): The parent page to which this unique ID property belongs.
        name (str): The name of the unique ID property.
        number (float): The number value of the unique ID.
        prefix (Optional[str]): The optional prefix of the unique ID.
        id_ (Optional[str]): The optional ID of the unique ID property.

    Returns:
        UniqueIdPage: A new UniqueIdPage object.
    """
    return _create_page_property(
        UniqueIdPage,
        parent=parent,
        property_type=PropertyType.UNIQUE_ID,
        name=name,
        id_=id_,
        unique_id=UniqueIdStructure(number=number, prefix=prefix)
    )
