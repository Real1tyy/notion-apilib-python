from abc import ABC

from pydantic import BaseModel, Field

from PropertyType import PropertyType


class PageProperty(ABC, BaseModel, from_attributes=True, use_enum_values=True):
    id: str = Field(exclude=True)
    type: PropertyType = Field(exclude=True)


class DatabaseProperty(PageProperty):
    description: str
    name: str
