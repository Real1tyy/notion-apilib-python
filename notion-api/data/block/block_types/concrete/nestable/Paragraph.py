from pydantic import BaseModel

from Block import Block


class ParagraphAttributes(BaseModel):
    rich_text: list
    color: str


class Paragraph(Block):
    paragraph: ParagraphAttributes
