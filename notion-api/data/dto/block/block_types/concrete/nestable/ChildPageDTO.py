from pydantic import UUID4

from block.block_types.BlockTypeDTO import BlockTypeDTO


class ChildPageDTO(BlockTypeDTO):
    page_id: UUID4
