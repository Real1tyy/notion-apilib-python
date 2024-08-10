# Third Party
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from _blocks.block import Block, BlockType
from structures import Emoji, RichText


class CalloutAttributes(BaseModel):
    """
    Attributes for a callout block.

    :param rich_text: A list of RichText objects representing the text content of the callout.
    :type rich_text: list[RichText]
    :param icon: An Emoji object representing the icon of the callout.
    :type icon: Emoji
    :param color: The color of the callout.
    :type color: str
    """
    rich_text: list[RichText]
    icon: Emoji
    color: str


class Callout(Block):
    """
    Represents a Callout block.

    :param callout: Attributes for the callout block.
    :type callout: CalloutAttributes
    """
    callout: CalloutAttributes

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.CALLOUT


class SyncedFrom(BaseModel):
    """
    Represents the source block that the synced block is synced from.

    :param block_id: The UUID of the source block.
    :type block_id: UUID
    """
    block_id: UUID


class SyncedBlockAttributes(BaseModel):
    """
    Attributes for synced _blocks.

    :param synced_from: The source block that this block is synced from.
    :type synced_from: Optional[SyncedFrom]
    :param children: List of child _blocks (default is an empty list).
    :type children: list[Block]
    """
    synced_from: Optional[SyncedFrom]
    children: list[Block] = []


class SyncedBlock(Block):
    """
    Represents a Synced block.

    :param synced_block: Attributes for the synced block.
    :type synced_block: SyncedBlockAttributes
    """
    synced_block: SyncedBlockAttributes

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.SYNCED_BLOCK


__all__ = ['Callout', 'SyncedBlock']
