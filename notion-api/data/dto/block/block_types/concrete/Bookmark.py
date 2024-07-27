from pydantic import HttpUrl, model_validator

from Block import Block
from custom_types import json_
from validation.exceptions import catch_exceptions


class Bookmark(Block):
    url: HttpUrl
    caption: list[str]

    @model_validator(mode='before')
    @classmethod
    @catch_exceptions
    def extract_block_type(cls, v: json_):
        bookmark = v.pop('bookmark')
        v['caption'] = bookmark['caption']
        v['url'] = bookmark['url']
        return v
