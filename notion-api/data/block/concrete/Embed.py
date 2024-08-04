from pydantic import BaseModel

from Block import Block, _create_block
from BlockType import BlockType
from Parent import Parent


class EmbedAttributes(BaseModel):
    url: str


class Embed(Block):
    embed: EmbedAttributes


def create_embed(parent: Parent, url: str) -> Embed:
    """
    Factory method to create Embed object
    :param parent: parent object
    :param url: URL for the embed
    :return: newly created Embed Object
    """
    return _create_block(
        Embed,
        parent=parent,
        block_type=BlockType.EMBED,
        embed=EmbedAttributes(url=url)
    )
