from typing import Any

from block_types.BlockType import BlockType
from general.ObjectDTO import ObjectDTO


class Block(ObjectDTO):
    type: BlockType
    has_children: bool
    children: list[Any] = []
