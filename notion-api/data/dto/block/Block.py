from typing import Any

from block_types.BlockType import BlockType
from general.Object import Object


class Block(Object):
    type: BlockType
    has_children: bool
    children: list[Any] = []
