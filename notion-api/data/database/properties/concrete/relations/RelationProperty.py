from typing import Annotated, Optional
from uuid import UUID

from pydantic import model_validator
from pydantic.types import UuidVersion

from custom_types import json_
from database.properties.Property import Property
from validation.exceptions import catch_exceptions


class RelationProperty(Property):
    database_id: Annotated[UUID, UuidVersion(4)]
    type: str

    synced_property_name: Optional[str] = None
    synced_property_id: Optional[str] = None

    @model_validator(mode='before')
    @classmethod
    @catch_exceptions
    def extract_relation_attributes(cls, v: json_):
        """
              Extracts and flattens the nested 'relation' and 'dual_property' attributes
              into the top-level dictionary for easy access for pydantic validation.
          """
        relation = v.pop('relation')
        v.update(relation)
        if 'dual_property' in v:
            dual_property = v.pop('dual_property')
            v.update(dual_property)
        return v
