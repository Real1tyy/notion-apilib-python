# Standard Library
from typing import Optional, Type

# Third Party
from Database import Database
from Page import Page
from PropertyType import PropertyType


def _create_page_property(
        cls: Type, parent: Page, property_type: PropertyType, name: str, id_: Optional[str] = None,
        **kwargs):
    """
    Helper function to create property objects with common parameters pre-filled.
    Also adds the newly created property to the Page associated with it
    :param cls: The class of the property object to create
    :param parent: The parent object
    :param property_type: The type of the property
    :param name: The name of the property
    :param id_: The id of the property
    :param kwargs: Additional keyword arguments specific to the property type
    :return: A new property object of the specified class
    """
    common_params = {
        "type": property_type,
        "name": name,
        "id": id_
    }
    property_ = cls(**common_params, **kwargs)
    parent.add_property(property_)
    return property_


def _create_database_property(
        cls: Type, parent: Database, property_type: PropertyType, name: str, id_: Optional[str] = None,
        **kwargs):
    """
    Helper function to create property objects with common parameters pre-filled.
    Also adds the newly created property to the Page associated with it
    :param cls: The class of the property object to create
    :param parent: The parent object
    :param property_type: The type of the property
    :param name: The name of the property
    :param id_: The id of the property
    :param kwargs: Additional keyword arguments specific to the property type
    :return: A new property object of the specified class
    """
    common_params = {
        "type": property_type,
        "name": name,
        "id": id_
    }
    property_ = cls(**common_params, **kwargs)
    parent.add_property(property_)
    return property_
