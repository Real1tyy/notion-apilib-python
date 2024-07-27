from pydantic import BaseModel

from database.properties.PropertyType import PropertyType


class Property(BaseModel, from_attributes=True, use_enum_values=True):
    id: str
    name: str
    type: PropertyType
