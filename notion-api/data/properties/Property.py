from abc import ABC

from pydantic import BaseModel, Field

from PropertyType import PropertyType
from custom_types import json_


class PageProperty(ABC, BaseModel, from_attributes=True, use_enum_values=True):
    id: str = Field(exclude=True)
    type: PropertyType = Field(exclude=True)
    name: str = Field(exclude=True)


class DatabaseProperty(PageProperty):
    description: str
    name: str


def create_page_property(data: json_) -> PageProperty:
    return PageProperty(**data)
