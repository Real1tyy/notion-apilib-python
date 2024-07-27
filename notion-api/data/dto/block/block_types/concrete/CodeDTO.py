from pydantic import model_validator

from BlockDTO import BlockDTO
from custom_types import json_
from validation.exceptions import catch_exceptions


class CodeDTO(BlockDTO):
    plain_text: str
    language: str
    caption: list[str]

    @model_validator(mode='before')
    @classmethod
    @catch_exceptions
    def extract_block_type(cls, v: json_):
        code = v.pop('code')
        v.update(code)
        rich_text = v.pop('rich_text')
        rich_text[0].pop('type')
        v.update(rich_text[0])
        return v
