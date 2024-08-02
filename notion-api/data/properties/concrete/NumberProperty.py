from pydantic import model_validator

from custom_types import json_
from database.properties.Property import Property
from validation.exceptions import catch_exceptions


class NumberProperty(Property):
    format: str

    @model_validator(mode='before')
    @classmethod
    @catch_exceptions
    def extract_relation_attributes(cls, v: json_):
        number = v.pop('number')
        v.update(number)
        return v
