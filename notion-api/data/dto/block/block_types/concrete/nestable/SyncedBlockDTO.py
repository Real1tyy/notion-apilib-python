from pydantic import UUID4

from block.block_types.BlockTypeDTO import BlockTypeDTO


class SyncedBlockDTO(BlockTypeDTO):
    synced_from: UUID4
