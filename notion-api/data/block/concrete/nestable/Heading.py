from pydantic import BaseModel

from Block import Block, _create_block
from BlockType import BlockType
from Parent import Parent
from RichText import RichText


class HeadingsAttributes(BaseModel):
    """
    Attributes for heading blocks.

    :param rich_text: List of rich text elements.
    :param color: Color of the heading text.
    :param is_toggleable: Whether the heading is toggleable.
    """
    rich_text: list[RichText]
    color: str
    is_toggleable: bool


class Heading1(Block):
    """
    Heading 1 block.

    :param heading_1: Attributes for the heading 1 block.
    """
    heading_1: HeadingsAttributes


class Heading2(Block):
    """
    Heading 2 block.

    :param heading_2: Attributes for the heading 2 block.
    """
    heading_2: HeadingsAttributes


class Heading3(Block):
    """
    Heading 3 block.

    :param heading_3: Attributes for the heading 3 block.
    """
    heading_3: HeadingsAttributes


def create_heading1(
        parent: Parent, rich_text: list[RichText], color: str, is_toggleable: bool,
        children: list[Block] = None) -> Heading1:
    """
    Factory method to create a Heading1 object.

    :param parent: The parent object.
    :param rich_text: The rich text content of the heading.
    :param color: The color of the heading.
    :param is_toggleable: Whether the heading is toggleable.
    :param children: List of child blocks (optional).
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
    :param children: List of child blocks (optional).
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
    :param children: List of child blocks (optional).
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
