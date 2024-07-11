from enum import Enum
from typing import Annotated
from uuid import UUID

from database.properties.PropertyDTO import PropertyDTO
from pydantic import model_validator
from pydantic.types import UuidVersion

from client.requests.types import json_


class RelationType(str, Enum):
    DUAL_PROPERTY = "dual_property"
    SINGLE_PROPERTY = "single_property"


class RelationPropertyDTO(PropertyDTO):
    database_id: Annotated[UUID, UuidVersion(4)]
    type: RelationType

    synced_property_name: str
    synced_property_id: str

    @model_validator(mode='before')
    @classmethod
    def extract_relation_attributes(cls, data: json_):
        return data['relation']

    # @field_validator('database_id')
    # @classmethod
    # @catch_exceptions
    # def related_database_validator(cls, str: Any) -> UUID:
    #     if related_database_id is None:
    #         raise ValueError("related_database_id cannot be None")
    #     return related_database_id
