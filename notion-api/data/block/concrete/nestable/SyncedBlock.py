# Standard Library
from typing import Optional
from uuid import UUID

# Third Party
from Block import Block, _create_block
from BlockType import BlockType
from Parent import Parent
from pydantic import BaseModel


class SyncedFrom(BaseModel):
    """
    Represents the source block that the synced block is synced from.

    :param block_id: The UUID of the source block.
    """
    block_id: UUID


class SyncedBlockAttributes(BaseModel):
    """
    Attributes for synced blocks.

    :param synced_from: The source block that this block is synced from.
    :param children: List of child blocks (default is an empty list).
    """
    synced_from: Optional[SyncedFrom]
    children: list[Block] = []


class SyncedBlock(Block):
    """
    Synced block.

    :param synced_block: Attributes for the synced block.
    """
    synced_block: SyncedBlockAttributes


def create_synced_block(
        parent: Parent, synced_from: Optional[SyncedFrom] = None,
        children: Optional[list[Block]] = None) -> SyncedBlock:
    """
    Factory method to create a SyncedBlock object.

    :param parent: The parent object.
    :param synced_from: The source block that this block is synced from (optional).
    :param children: List of child blocks (optional).
    :return: A new SyncedBlock object.
    """
    return _create_block(
        SyncedBlock,
        parent=parent,
        block_type=BlockType.SYNCED_BLOCK,
        synced_block=SyncedBlockAttributes(
            synced_from=synced_from,
            children=children
        ),
        children=children
    )
