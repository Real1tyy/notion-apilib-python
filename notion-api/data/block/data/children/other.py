# Third Party
from pydantic import BaseModel

from Emoji import Emoji
from Parent import Parent
from RichText import RichText
from block import Block, _create_block
from type import BlockType


class CalloutAttributes(BaseModel):
    rich_text: list[RichText]
    icon: Emoji
    color: str


class Callout(Block):
    callout: CalloutAttributes


def create_callout(
        parent: Parent, rich_text: list[RichText], icon: Emoji, color: str,
        children: list['Block'] = None) -> Callout:
    """
    Factory method to create Callout object
    :param parent: parent object
    :param rich_text: rich text for the callout
    :param icon: icon for the callout
    :param color: color of the callout
    :param children: optional list of child blocks
    :return: newly created Callout Object
    """
    return _create_block(
        Callout,
        parent=parent,
        block_type=BlockType.CALLOUT,
        children=children,
        callout=CalloutAttributes(
            rich_text=rich_text,
            icon=icon,
            color=color
        )
    )


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
