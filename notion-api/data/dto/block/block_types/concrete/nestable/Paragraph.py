from pydantic import model_validator

from Block import Block
from block_types.rich_text_validation import validate_rich_text
from custom_types import json_


class Paragraph(Block):
    plain_text: str

    @model_validator(mode='before')
    @classmethod
    def extract_block_type(cls, v: json_):
        return validate_rich_text(v)
