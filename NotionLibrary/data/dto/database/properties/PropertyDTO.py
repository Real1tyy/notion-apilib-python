from pydantic import BaseModel, ConfigDict

from database.properties.PropertyTypes import PropertyTypes


class PropertyDTO(BaseModel):
    model_config: ConfigDict = ConfigDict(from_attributes=True)

    id: str
    name: str
    type: PropertyTypes
