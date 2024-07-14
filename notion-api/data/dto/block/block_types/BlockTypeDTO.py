from pydantic import BaseModel

from block_types.BlockType import BlockType


class BlockTypeDTO(BaseModel):
    type: BlockType
