from pydantic import model_validator

from custom_types import json_
from database.properties.PropertyDTO import PropertyDTO
from validation.exceptions import catch_exceptions


class FormulaPropertyDTO(PropertyDTO):
    expression: str

    @model_validator(mode='before')
    @classmethod
    @catch_exceptions
    def extract_relation_attributes(cls, v: json_):
        formula = v.pop('formula')
        v.update(formula)
        return v
