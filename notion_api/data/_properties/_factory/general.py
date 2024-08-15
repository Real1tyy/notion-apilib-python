# Standard Library
from typing import Type, TypeVar, Any, Optional

# Third Party
from notion_api.data._properties.property import PageProperty, DatabaseProperty, Property

T = TypeVar('T', bound=Property)
T2 = TypeVar('T2', bound=PageProperty)
T3 = TypeVar('T3', bound=DatabaseProperty)


def _create_property(
        cls: Type[T], parent: 'MajorObject', name: str, property_specific_params: Optional[Any] = None) -> T:
    """
    Helper function to create property objects with common parameters pre-filled.
    Also adds the newly created property to the Page associated with it
    :param cls: The class of the property object to create
    :param parent: The parent object - Page or Database
    :param name: The name of the property
    :param property_specific_params: Additional keyword arguments specific to the property type
    :return: A new property object of the specified class
    """
    common_params = {
        "type": cls.get_associated_property_type(),
        "name": name,
    }
    if property_specific_params:
        payload_property_name = cls.get_payload_property_name()
        common_params[payload_property_name] = property_specific_params

    property_ = cls(**common_params)
    parent.add_property(property_)
    return property_


def _create_page_property(
        cls: Type[T2], parent: 'Page', name: str, property_specific_params: Optional[Any] = None) -> T2:
    """
    Helper function to create property objects with common parameters pre-filled.
    Also adds the newly created property to the Page associated with it
    :param cls: The class of the property object to create
    :param parent: The parent object
    :param name: The name of the property
    :param property_specific_params: Additional keyword arguments specific to the property type
    :return: A new property object of the specified class
    """
    return _create_property(cls, parent, name, property_specific_params)


def _create_database_property(
        cls: Type[T3], parent: 'Database', name: str, property_specific_params: Optional[Any] = None) -> T3:
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
    return _create_property(cls, parent, name, property_specific_params)
