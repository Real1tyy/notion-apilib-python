from pydantic import UUID4

from block.block_types.BlockTypeDTO import BlockTypeDTO


class ChildDatabaseDTO(BlockTypeDTO):
    database_id: UUID4
