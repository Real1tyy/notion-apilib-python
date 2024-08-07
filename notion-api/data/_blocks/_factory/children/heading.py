from typing import Type, Optional, TypeVar, Union

from structures import Parent, RichText, create_basic_rich_text
from block import Block
from _blocks.data import HeadingsAttributes, Heading1, Heading2, Heading3
from _blocks._factory.general import _create_block

T = TypeVar('T', Heading1, Heading2, Heading3)


def create_headings_attributes(rich_text: list[RichText], color: str, is_toggleable: bool) -> HeadingsAttributes:
    """
    Factory method to create a HeadingsAttributes object.

    :param rich_text: List of rich text elements.
    :param color: Color of the heading text.
    :param is_toggleable: Whether the heading is toggleable.
    :return: A new HeadingsAttributes instance.
    """
    return HeadingsAttributes(
        rich_text=rich_text,
        color=color,
        is_toggleable=is_toggleable
    )


def create_heading(
        heading_type: Type[T], parent: Parent, rich_text: list[RichText], color: str, is_toggleable: bool,
        children: Optional[list[Block]] = None) -> T:
    """
    Factory method to create a heading object.

    :param heading_type: The type of the heading block (Heading1, Heading2, or Heading3).
    :param parent: The parent object.
    :param rich_text: The rich text content of the heading.
    :param color: The color of the heading.
    :param is_toggleable: Whether the heading is toggleable.
    :param children: List of child blocks (optional).
    :return: A new heading object of the specified type.
    """
    return _create_block(
        heading_type,
        parent=parent,
        block_type_specific_params=create_headings_attributes(rich_text, color, is_toggleable),
        children=children
    )


def create_basic_heading(
        heading_type: Type[T], parent: Parent, text: str, is_toggleable: bool,
        children: Optional[list[Block]] = None) -> T:
    """
    Factory method to create a basic heading object.

    :param heading_type: The type of the heading block (Heading1, Heading2, or Heading3).
    :param parent: The parent object.
    :param text: The text content of the heading.
    :param is_toggleable: Whether the heading is toggleable.
    :param children: List of child blocks (optional).
    :return: A new heading object of the specified type.
    """
    heading_attributes = create_headings_attributes([create_basic_rich_text(text)], "default", is_toggleable)
    return _create_block(
        heading_type,
        parent=parent,
        block_type_specific_params=heading_attributes,
        children=children,
    )
