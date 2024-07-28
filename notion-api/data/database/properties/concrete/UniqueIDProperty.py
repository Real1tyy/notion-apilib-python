from pydantic import model_validator

from custom_types import json_
from database.properties.Property import Property
from validation.exceptions import catch_exceptions


class UniqueIDProperty(Property):
    prefix: str

    @model_validator(mode='before')
    @classmethod
    @catch_exceptions
    def extract_relation_attributes(cls, v: json_):
        unique_id = v.pop('unique_id')
        v.update(unique_id)
        return v
