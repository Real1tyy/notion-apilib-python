# Standard Library
from typing import Optional, Type, TypeVar

from .._general import _create_block

# First Party
from ...data import Heading1, Heading2, Heading3, block_structures
from ...block import Block
from notion_api.data.structures import Parent, RichText, create_basic_rich_text

T = TypeVar("T", Heading1, Heading2, Heading3)


def create_headings_attributes(
    rich_text: list[RichText], color: str, is_toggleable: bool
) -> block_structures.HeadingsAttributes:
    """
    Factory method to create a HeadingsAttributes object.

    :param rich_text: List of rich text elements.
    :param color: Color of the heading text.
    :param is_toggleable: Whether the heading is toggleable.
    :return: A new HeadingsAttributes instance.
    """
    return block_structures.HeadingsAttributes(
        rich_text=rich_text, color=color, is_toggleable=is_toggleable
    )


def create_heading(
    heading_type: Type[T],
    parent: Parent,
    rich_text: list[RichText],
    color: str,
    is_toggleable: bool,
    children: Optional[list[Block]] = None,
) -> T:
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
        children=children,
        block_type_specific_params=create_headings_attributes(
            rich_text, color, is_toggleable
        ),
    )


def create_basic_heading(
    heading_type: Type[T],
    parent: Parent,
    text: str,
    is_toggleable: bool,
    children: Optional[list[Block]] = None,
) -> T:
    """
    Factory method to create a basic heading object.

    :param heading_type: The type of the heading block (Heading1, Heading2, or Heading3).
    :param parent: The parent object.
    :param text: The text content of the heading.
    :param is_toggleable: Whether the heading is toggleable.
    :param children: List of child blocks (optional).
    :return: A new heading object of the specified type.
    """
    return create_heading(
        heading_type,
        parent,
        [create_basic_rich_text(text)],
        "default",
        is_toggleable,
        children,
    )


def create_basic_heading1(
    parent: Parent,
    text: str,
    is_toggleable: bool,
    children: Optional[list[Block]] = None,
) -> Heading1:
    """
    Factory method to create a basic Heading1 object.

    :param parent: The parent object.
    :param text: The text content of the heading.
    :param is_toggleable: Whether the heading is toggleable.
    :param children: List of child blocks (optional).
    :return: A new Heading1 object.
    """
    return create_basic_heading(Heading1, parent, text, is_toggleable, children)


def create_basic_heading2(
    parent: Parent,
    text: str,
    is_toggleable: bool,
    children: Optional[list[Block]] = None,
) -> Heading2:
    """
    Factory method to create a basic Heading2 object.

    :param parent: The parent object.
    :param text: The text content of the heading.
    :param is_toggleable: Whether the heading is toggleable.
    :param children: List of child blocks (optional).
    :return: A new Heading2 object.
    """
    return create_basic_heading(Heading2, parent, text, is_toggleable, children)


def create_basic_heading3(
    parent: Parent,
    text: str,
    is_toggleable: bool,
    children: Optional[list[Block]] = None,
) -> Heading3:
    """
    Factory method to create a basic Heading3 object.

    :param parent: The parent object.
    :param text: The text content of the heading.
    :param is_toggleable: Whether the heading is toggleable.
    :param children: List of child blocks (optional).
    :return: A new Heading3 object.
    """
    return create_basic_heading(Heading3, parent, text, is_toggleable, children)


def create_heading1(
    parent: Parent,
    rich_text: list[RichText],
    color: str,
    is_toggleable: bool,
    children: Optional[list[Block]] = None,
) -> Heading1:
    """
    Factory method to create a Heading1 object.

    :param parent: The parent object.
    :param rich_text: The rich text content of the heading.
    :param color: The color of the heading.
    :param is_toggleable: Whether the heading is toggleable.
    :param children: List of child blocks (optional).
    :return: A new Heading1 object.
    """
    return create_heading(Heading1, parent, rich_text, color, is_toggleable, children)


def create_heading2(
    parent: Parent,
    rich_text: list[RichText],
    color: str,
    is_toggleable: bool,
    children: Optional[list[Block]] = None,
) -> Heading2:
    """
    Factory method to create a Heading2 object.

    :param parent: The parent object.
    :param rich_text: The rich text content of the heading.
    :param color: The color of the heading.
    :param is_toggleable: Whether the heading is toggleable.
    :param children: List of child blocks (optional).
    :return: A new Heading2 object.
    """
    return create_heading(Heading2, parent, rich_text, color, is_toggleable, children)


def create_heading3(
    parent: Parent,
    rich_text: list[RichText],
    color: str,
    is_toggleable: bool,
    children: Optional[list[Block]] = None,
) -> Heading3:
    """
    Factory method to create a Heading3 object.

    :param parent: The parent object.
    :param rich_text: The rich text content of the heading.
    :param color: The color of the heading.
    :param is_toggleable: Whether the heading is toggleable.
    :param children: List of child blocks (optional).
    :return: A new Heading3 object.
    """
    return create_heading(Heading3, parent, rich_text, color, is_toggleable, children)


__all__ = [
    "create_heading1",
    "create_heading2",
    "create_heading3",
    "create_basic_heading1",
    "create_basic_heading2",
    "create_basic_heading3",
]
