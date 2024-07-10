from enum import Enum
from typing import Annotated
from uuid import UUID

from pydantic import BeforeValidator, model_validator
from pydantic.types import UuidVersion

from client.requests.types import json_
from database.properties.PropertyDTO import PropertyDTO


class RelationType(str, Enum):
    DUAL_PROPERTY = "dual_property"
    SINGLE_PROPERTY = "single_property"


class RelationPropertyDTO(PropertyDTO):
    database_id: Annotated[UUID, UuidVersion(4), BeforeValidator(related_database_validator)]
    type: RelationType

    synced_property_name: str
    synced_property_id: str

    @model_validator(mode='before')
    def extract_relation_attributes(cls, data: json_):
        return data['relation']
