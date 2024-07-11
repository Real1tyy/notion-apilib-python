from pydantic import model_validator, Field

from RollupFunction import RollupFunction
from custom_types import json_
from database.properties.PropertyDTO import PropertyDTO
from validation.exceptions import catch_exceptions


class RollupPropertyDTO(PropertyDTO):
    function: RollupFunction = Field(
        ..., description="The function that computes the rollup value from the related pages.")
    relation_property_id: str = Field(..., description="The id of the related database property that is rolled up.")
    relation_property_name: str = Field(..., description="The name of the related database property that is rolled up.")
    rollup_property_id: str = Field(..., description="The id of the rollup property.")
    rollup_property_name: str = Field(..., description="The name of the rollup property.")

    @model_validator(mode='before')
    @classmethod
    @catch_exceptions
    def extract_relation_attributes(cls, v: json_):
        rollup = v.pop('rollup')
        v.update(rollup)
        return v
