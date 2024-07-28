from Block import Block
from Emoji import Emoji
from RichText import RichText


class Callout(Block):
    rich_text: list[RichText]
    icon: Emoji
    color: str
