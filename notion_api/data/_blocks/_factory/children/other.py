from typing import Optional

from structures import Parent, RichText, Emoji
from _blocks.block import Block
from _blocks._factory.general import _create_block
from _blocks._data.children.other import SyncedFrom, SyncedBlock, SyncedBlockAttributes, Callout, CalloutAttributes


def create_callout(
        parent: Parent, rich_text: list[RichText], icon: Emoji, color: str,
        children: list['Block'] = None) -> Callout:
    """
    Factory method to create Callout object
    :param parent: parent object
    :param rich_text: rich text for the callout
    :param icon: icon for the callout
    :param color: color of the callout
    :param children: optional list of child _blocks
    :return: newly created Callout Object
    """
    return _create_block(
        Callout,
        parent=parent,
        children=children,
        block_type_specific_params=CalloutAttributes(
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
    :param synced_from: The source _blocks that this _blocks is synced from (optional).
    :param children: List of child _blocks (optional).
    :return: A new SyncedBlock object.
    """
    return _create_block(
        SyncedBlock,
        parent=parent,
        block_type_specific_params=SyncedBlockAttributes(
            synced_from=synced_from,
            children=children
        ),
        children=children
    )


__all__ = [
    'create_callout', 'create_synced_block'
]
