from abc import ABC

from pydantic import BaseModel, Field

from PropertyType import PropertyType
from custom_types import json_


class Property(ABC, BaseModel, from_attributes=True, use_enum_values=True):
    id: str = Field(exclude=True)
    type: PropertyType = Field(exclude=True)


class PageProperty(Property):
    name: str = Field(exclude=True)


class DatabaseProperty(Property):
    name: str = Field(exclude=True)


def create_page_property(data: json_) -> PageProperty:
    return PageProperty(**data)
