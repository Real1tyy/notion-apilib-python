from pydantic import BaseModel

from NotionLibrary.data.dto.database.properties.PropertyTypes import PropertyTypes


class PropertyDTO(BaseModel, from_attributes=True):
    id: str
    name: str
    type: PropertyTypes
