# Standard Library
from abc import ABC

# Third Party
from type import PropertyType
from pydantic import BaseModel, Field


class Property(ABC, BaseModel, from_attributes=True, use_enum_values=True):
    id: str = Field(exclude=True)
    type: PropertyType = Field(exclude=True)
    name: str = Field(exclude=True)


class PageProperty(Property):
    pass


class DatabaseProperty(Property):
    pass
