from pydantic import BaseModel

from database.properties.PropertyTypes import PropertyTypes


class PropertyDTO(BaseModel, from_attributes=True, use_enum_values=True):
    id: str
    name: str
    type: PropertyTypes
