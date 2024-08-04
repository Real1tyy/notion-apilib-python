from _data.Parent import Parent
from _data.RichText import RichText
from block import Block, _create_block
from heading import Heading1, HeadingsAttributes, Heading2, Heading3
from type import BlockType


def create_heading1(
        parent: Parent, rich_text: list[RichText], color: str, is_toggleable: bool,
        children: list[Block] = None) -> Heading1:
    """
    Factory method to create a Heading1 object.

    :param parent: The parent object.
    :param rich_text: The rich text content of the heading.
    :param color: The color of the heading.
    :param is_toggleable: Whether the heading is toggleable.
    :param children: List of child _blocks (optional).
    :return: A new Heading1 object.
    """
    return _create_block(
        Heading1,
        parent=parent,
        block_type=BlockType.HEADING_1,
        heading_1=HeadingsAttributes(
            rich_text=rich_text,
            color=color,
            is_toggleable=is_toggleable
        ),
        children=children
    )


def create_heading2(
        parent: Parent, rich_text: list[RichText], color: str, is_toggleable: bool,
        children: list[Block] = None) -> Heading2:
    """
    Factory method to create a Heading2 object.

    :param parent: The parent object.
    :param rich_text: The rich text content of the heading.
    :param color: The color of the heading.
    :param is_toggleable: Whether the heading is toggleable.
    :param children: List of child _blocks (optional).
    :return: A new Heading2 object.
    """
    return _create_block(
        Heading2,
        parent=parent,
        block_type=BlockType.HEADING_2,
        heading_2=HeadingsAttributes(
            rich_text=rich_text,
            color=color,
            is_toggleable=is_toggleable
        ),
        children=children
    )


def create_heading3(
        parent: Parent, rich_text: list[RichText], color: str, is_toggleable: bool,
        children: list[Block] = None) -> Heading3:
    """
    Factory method to create a Heading3 object.

    :param parent: The parent object.
    :param rich_text: The rich text content of the heading.
    :param color: The color of the heading.
    :param is_toggleable: Whether the heading is toggleable.
    :param children: List of child _blocks (optional).
    :return: A new Heading3 object.
    """
    return _create_block(
        Heading3,
        parent=parent,
        block_type=BlockType.HEADING_3,
        heading_3=HeadingsAttributes(
            rich_text=rich_text,
            color=color,
            is_toggleable=is_toggleable
        ),
        children=children
    )
