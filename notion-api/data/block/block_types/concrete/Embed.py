from pydantic import BaseModel

from Block import Block


class EmbedAttributes(BaseModel):
    url: str


class Embed(Block):
    embed: EmbedAttributes
