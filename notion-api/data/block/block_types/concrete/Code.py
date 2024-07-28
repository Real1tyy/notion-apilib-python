from pydantic import BaseModel

from Block import Block
from RichText import RichText


class CodeAttributes(BaseModel):
    caption: list[RichText]
    rich_text: list[RichText]
    language: str


class Code(Block):
    code: CodeAttributes
