from pydantic import model_validator

from block.block_types.BlockTypeDTO import BlockTypeDTO
from custom_types import json_
from validation.exceptions import catch_exceptions


class CodeDTO(BlockTypeDTO):
    text: str
    language: str

    @model_validator(mode='before')
    @classmethod
    @catch_exceptions
    def extract_block_type(cls, v: json_):
        rich_text = v.pop('rich_text')
        print(rich_text)
        v['text'] = rich_text[0]['text']['content']
        return v
