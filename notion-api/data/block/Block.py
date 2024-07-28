from abc import ABC

from pydantic import Field

from Object import Object
from block_types.BlockType import BlockType


class Block(Object, ABC):
    type: BlockType
    has_children: bool
    children: list['Block'] = Field(default=[], exclude=True)
