from pydantic import model_validator

from custom_types import json_
from database.properties.Property import Property
from validation.exceptions import catch_exceptions


class RollupProperty(Property):
    function: str
    relation_property_id: str
    relation_property_name: str
    rollup_property_id: str
    rollup_property_name: str

    @model_validator(mode='before')
    @classmethod
    @catch_exceptions
    def extract_relation_attributes(cls, v: json_):
        rollup = v.pop('rollup')
        v.update(rollup)
        return v
