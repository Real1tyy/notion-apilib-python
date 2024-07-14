from typing import Annotated, Any

from pydantic import model_validator, BeforeValidator

from block_types.BlockType import BlockType
from custom_types import json_
from general.ObjectDTO import ObjectDTO
from validation.exceptions import catch_exceptions
from validation.validators import block_type_validator


class BlockDTO(ObjectDTO):
    type: BlockType
    has_children: bool
    block_type: Annotated[Any, BeforeValidator(block_type_validator)]

    @model_validator(mode='before')
    @classmethod
    @catch_exceptions
    def extract_block_type(cls, v: json_):
        type_ = v['type']
        block_type = v.pop(type_)
        block_type['type'] = type_
        v['block_type'] = block_type
        return v
