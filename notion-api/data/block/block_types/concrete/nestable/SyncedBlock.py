from pydantic import UUID4

from Block import Block


class SyncedBlock(Block):
    synced_from: UUID4
