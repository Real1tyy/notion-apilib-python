from typing import Optional

from Emoji import Emoji
from Parent import Parent
from RichText import RichText
from blocks.block import Block, _create_block
from other import SyncedFrom, SyncedBlock, SyncedBlockAttributes, Callout, CalloutAttributes
from type import BlockType


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


def create_synced_block(
        parent: Parent, synced_from: Optional[SyncedFrom] = None,
        children: Optional[list[Block]] = None) -> SyncedBlock:
    """
    Factory method to create a SyncedBlock object.

    :param parent: The parent object.
    :param synced_from: The source blocks that this blocks is synced from (optional).
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
