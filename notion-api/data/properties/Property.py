from abc import ABC

from pydantic import BaseModel

from PropertyType import PropertyType


class PageProperty(ABC, BaseModel, from_attributes=True, use_enum_values=True):
    id: str
    name: str
    type: PropertyType
