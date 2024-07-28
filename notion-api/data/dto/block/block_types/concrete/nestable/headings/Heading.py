from abc import ABC

from pydantic import model_validator

from Block import Block
from block_types.concrete.nestable.headings.HeadingColor import HeadingColor
from custom_types import json_
from validation.exceptions import catch_exceptions


class Heading(ABC, Block):
    text: str
    color: HeadingColor
    is_toggleable: bool

    @model_validator(mode='before')
    @classmethod
    @catch_exceptions
    def extract(cls, v: json_):
        rich_text = v['rich_text'][0]
        text = rich_text.pop('text')
        text = text['content']
        v['text'] = text
        return v
