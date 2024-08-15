# Standard Library
from abc import ABC, abstractmethod
from typing import Literal, Any
from uuid import UUID

from pydantic import BaseModel, Field

# Third Party
from notion_api.data._properties.type_ import PropertyType
from notion_api.data.configuration import BasicConfiguration
from notion_api.data._properties.sort import PropertySort


class Property(BasicConfiguration, ABC):
    """
    Abstract base class representing a property in the Notion API.

    Attributes
    ----------
    id : str
        The unique identifier of the property (excluded from serialization).
    type : PropertyType
        The type of the property (excluded from serialization).
    name : str
        The name of the property (excluded from serialization).
    """
    id: UUID = Field(exclude=True)
    type: PropertyType = Field(exclude=True)
    name: str = Field(exclude=True)

    @classmethod
    @abstractmethod
    def get_associated_property_type(cls) -> PropertyType:
        """
        Retrieves the property type associated with this class.

        :return: The associated property type enum value.
        :rtype: PropertyType
        """
        pass

    @classmethod
    def get_payload_property_name(cls) -> str:
        """
        Retrieves the property name of the property type as a string, which is used in the Notion JSON format.
        Utilizes the get_associated_block_type method to obtain the enum value and converts it to a string.

        :return: The property name of the block type as a string.
        :rtype: str
        """
        return cls.get_associated_property_type().value

    def serialize_to_json(self):
        return self.model_dump(mode='json', exclude_none=True)


class PageProperty(Property, ABC):
    """
    Class representing a page property in the Notion API.
    """


class DatabaseProperty(Property, ABC):
    """
    Class representing a database property in the Notion API.
    """

    def create_sort_object(self, direction: Literal['ascending', 'descending']) -> PropertySort:
        """
          Creates a sort object for the property with the specified sort direction.
        :param direction:
        :return: PropertySort object representing the sort object
        """
        return PropertySort(direction=direction, property=self.name)


__all__ = [
    'PageProperty', 'DatabaseProperty', 'PropertyType', 'Property']
