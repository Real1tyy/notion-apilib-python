from abc import ABC
from typing import Any

from Object import Object
from block_types.BlockType import BlockType


class Block(Object, ABC):
    type: BlockType
    has_children: bool
    children: list[Any] = None
