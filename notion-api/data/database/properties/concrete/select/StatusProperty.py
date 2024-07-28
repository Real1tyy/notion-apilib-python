from pydantic import model_validator

from Option import Option
from custom_types import json_
from database.properties.Property import Property
from validation.exceptions import catch_exceptions


class StatusProperty(Property):
    options: list[Option]

    @model_validator(mode='before')
    @classmethod
    @catch_exceptions
    def extract_relation_attributes(cls, v: json_):
        status = v.pop('status')
        v.update(status)
        return v
