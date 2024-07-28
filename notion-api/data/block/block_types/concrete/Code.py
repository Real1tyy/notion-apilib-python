from Block import Block
from RichText import RichText


class Code(Block):
    caption: list[RichText]
    rich_text: list[RichText]
    language: str
