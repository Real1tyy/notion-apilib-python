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
