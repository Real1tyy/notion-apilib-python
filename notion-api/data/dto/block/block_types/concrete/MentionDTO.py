from pydantic import UUID4

from block_types.BlockTypeDTO import BlockTypeDTO


class MentionDTO(BlockTypeDTO):
    type: str
    id: UUID4
