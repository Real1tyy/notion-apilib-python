from block.BlockType import BlockType
from general.ObjectDTO import ObjectDTO


class BlockDTO(ObjectDTO):
    type: BlockType
    has_children: bool
