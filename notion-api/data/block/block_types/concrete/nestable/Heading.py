from pydantic import BaseModel

from Block import Block
from RichText import RichText


class HeadingsAttributes(BaseModel):
    rich_text: list[RichText]
    color: str
    is_toggleable: bool


class Heading1(Block):
    heading_1: HeadingsAttributes


class Heading2(Block):
    heading_2: HeadingsAttributes


class Heading3(Block):
    heading_3: HeadingsAttributes
