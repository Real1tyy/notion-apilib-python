from pydantic import BaseModel

from Block import Block
from RichText import RichText


class ParagraphAttributes(BaseModel):
    rich_text: list[RichText]
    color: str


class Paragraph(Block):
    paragraph: ParagraphAttributes
