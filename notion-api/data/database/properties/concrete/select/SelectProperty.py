from pydantic import model_validator

from Option import Option
from custom_types import json_
from database.properties.Property import Property
from validation.exceptions import catch_exceptions


class SelectProperty(Property):
    options: list[Option]

    @model_validator(mode='before')
    @classmethod
    @catch_exceptions
    def extract_relation_attributes(cls, v: json_):
        select = v.pop('data/database/properties/concrete/select')
        v.update(select)
        return v
