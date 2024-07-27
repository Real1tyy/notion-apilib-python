from pydantic import model_validator

from Option import Option
from custom_types import json_
from database.properties.Property import Property
from validation.exceptions import catch_exceptions


class MultiSelectProperty(Property):
    options: list[Option]

    @model_validator(mode='before')
    @classmethod
    @catch_exceptions
    def extract_relation_attributes(cls, v: json_):
        multi_select = v.pop('multi_select')
        v.update(multi_select)
        return v
