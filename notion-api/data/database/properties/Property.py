from abc import ABC

from pydantic import BaseModel

from database.properties.PropertyType import PropertyType


class Property(ABC, BaseModel, from_attributes=True, use_enum_values=True):
    id: str
    name: str
    type: PropertyType
