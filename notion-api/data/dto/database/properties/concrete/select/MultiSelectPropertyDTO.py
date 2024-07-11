from pydantic import model_validator

from OptionDTO import OptionDTO
from custom_types import json_
from database.properties.PropertyDTO import PropertyDTO
from validation.exceptions import catch_exceptions


class MultiSelectPropertyDTO(PropertyDTO):
    options: list[OptionDTO]

    @model_validator(mode='before')
    @classmethod
    @catch_exceptions
    def extract_relation_attributes(cls, v: json_):
        multi_select = v.pop('multi_select')
        v.update(multi_select)
        return v
