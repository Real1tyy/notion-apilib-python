from typing import Optional, Annotated
from uuid import UUID

from pydantic import BaseModel
from pydantic.types import UuidVersion

from Block import Block


class SyncedFrom(BaseModel):
    block_id: Annotated[UUID, UuidVersion(4)]


class SyncedBlockAttributes(BaseModel):
    synced_from: Optional[SyncedFrom]
    children: list[Block] = []


class SyncedBlock(Block):
    synced_block: SyncedBlockAttributes
