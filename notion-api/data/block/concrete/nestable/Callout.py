from pydantic import BaseModel

from Block import Block
from Emoji import Emoji
from RichText import RichText


class CalloutAttributes(BaseModel):
    rich_text: list[RichText]
    icon: Emoji
    color: str


class Callout(Block):
    callout: CalloutAttributes
