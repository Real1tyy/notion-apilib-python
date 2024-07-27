from pydantic import UUID4

from BlockDTO import BlockDTO


class SyncedBlockDTO(BlockDTO):
    synced_from: UUID4
