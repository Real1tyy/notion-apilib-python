from pydantic import model_validator

from OptionDTO import OptionDTO
from custom_types import json_
from database.properties.PropertyDTO import PropertyDTO
from validation.exceptions import catch_exceptions


class SelectPropertyDTO(PropertyDTO):
    options: list[OptionDTO]

    @model_validator(mode='before')
    @classmethod
    @catch_exceptions
    def extract_relation_attributes(cls, v: json_):
        select = v.pop('select')
        v.update(select)
        return v
