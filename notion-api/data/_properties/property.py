# Standard Library
from abc import ABC

from pydantic import BaseModel, Field

# Third Party
from type_ import PropertyType


class Property(ABC, BaseModel, from_attributes=True, use_enum_values=True):
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
    id: str = Field(exclude=True)
    type: PropertyType = Field(exclude=True)
    name: str = Field(exclude=True)


class PageProperty(Property):
    """
    Class representing a page property in the Notion API.
    """
    pass


class DatabaseProperty(Property):
    """
    Class representing a database property in the Notion API.
    """
    pass
