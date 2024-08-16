# Standard Library
from typing import Optional, Type, TypeVar

from .._general import _create_block

# First Party
from ...data import (
    BulletedListItem,
    NumberedListItem,
    Paragraph,
    Quote,
    ToDo,
    Toggle,
    block_structures,
)
from ...block import Block
from notion_api.data.structures import Parent, RichText, create_basic_rich_text

T = TypeVar("T", BulletedListItem, NumberedListItem, Paragraph, Quote, Toggle)


def _create_items_attribute(
    rich_text: list[RichText], color: str, children: Optional[list[Block]] = None
) -> block_structures.Items:
    """
    Factory method to create an Items object.

    :param rich_text: List of rich text elements.
    :param color: Color of the item text.
    :param children: List of child blocks (optional).
    :return: A new Items instance.
    """
    return block_structures.Items(rich_text=rich_text, color=color, children=children)


def _create_item(
    item_type: Type[T],
    parent: Parent,
    color: str,
    rich_text: list[RichText],
    children: Optional[list[Block]] = None,
) -> T:
    """
    Factory method to create an item block object.

    :param item_type: The type of the item block (BulletedListItem, NumberedListItem, Paragraph, Quote, or Toggle).
    :param parent: The parent object.
    :param color: The color of the item text.
    :param rich_text: The rich text content of the item.
    :param children: List of child blocks (optional).
    :return: A new item block object of the specified type.
    """
    return _create_block(
        item_type,
        parent=parent,
        children=children,
        block_type_specific_params=_create_items_attribute(rich_text, color, children),
    )


def create_bulleted_list_item(
    parent: Parent, color: str, rich_text: list[RichText], children: list[Block] = None
) -> BulletedListItem:
    """
    Factory method to create a BulletedListItem object.

    :param parent: The parent object.
    :param color: The color of the item text.
    :param rich_text: The rich text content of the item.
    :param children: List of child blocks (optional).
    :return: A new BulletedListItem object.
    """
    return _create_item(BulletedListItem, parent, color, rich_text, children)


def create_numbered_list_item(
    parent: Parent, color: str, rich_text: list[RichText], children: list[Block] = None
) -> NumberedListItem:
    """
    Factory method to create a NumberedListItem object.

    :param parent: The parent object.
    :param color: The color of the item text.
    :param rich_text: The rich text content of the item.
    :param children: List of child blocks (optional).
    :return: A new NumberedListItem object.
    """
    return _create_item(NumberedListItem, parent, color, rich_text, children)


def create_basic_paragraph(
    parent: Parent, text: str, children: list[Block] = None
) -> Paragraph:
    """
    Factory method to create a basic Paragraph object.

    :param parent: The parent object.
    :param text: The text content of the paragraph.
    :param children: List of child blocks (optional).
    :return: A new Paragraph object.
    """
    return _create_item(
        Paragraph, parent, "default", [create_basic_rich_text(text)], children
    )


def create_paragraph(
    parent: Parent, color: str, rich_text: list[RichText], children: list[Block] = None
) -> Paragraph:
    """
    Factory method to create a Paragraph object.

    :param parent: The parent object.
    :param color: The color of the paragraph text.
    :param rich_text: The rich text content of the paragraph.
    :param children: List of child blocks (optional).
    :return: A new Paragraph object.
    """
    return _create_item(Paragraph, parent, color, rich_text, children)


def create_quote(
    parent: Parent, color: str, rich_text: list[RichText], children: list[Block] = None
) -> Quote:
    """
    Factory method to create a Quote object.

    :param parent: The parent object.
    :param color: The color of the quote text.
    :param rich_text: The rich text content of the quote.
    :param children: List of child blocks (optional).
    :return: A new Quote object.
    """
    return _create_item(Quote, parent, color, rich_text, children)


def create_toggle(
    parent: Parent, color: str, rich_text: list[RichText], children: list[Block] = None
) -> Toggle:
    """
    Factory method to create a Toggle object.

    :param parent: The parent object.
    :param color: The color of the toggle text.
    :param rich_text: The rich text content of the toggle.
    :param children: List of child blocks (optional).
    :return: A new Toggle object.
    """
    return _create_item(Toggle, parent, color, rich_text, children)


def create_to_do(
    parent: Parent,
    color: str,
    rich_text: list[RichText],
    checked: Optional[bool] = None,
    children: list[Block] = None,
) -> ToDo:
    """
    Factory method to create a ToDo object.

    :param parent: The parent object.
    :param color: The color of the to-do text.
    :param rich_text: The rich text content of the to-do item.
    :param checked: Whether the to-do item is checked (optional).
    :param children: List of child _blocks (optional).
    :return: A new ToDo object.
    """
    return _create_block(
        ToDo,
        parent=parent,
        children=children,
        block_type_specific_params=block_structures.ToDoAttributes(
            color=color,
            rich_text=rich_text,
            checked=checked,
            children=children if children else [],
        ),
    )


def _create_basic_item(
    item_type: Type[T], parent: Parent, text: str, children: list[Block] = None
) -> T:
    """
    Factory method to create an item block object.

    :param item_type: The type of the item block (BulletedListItem, NumberedListItem, Paragraph, Quote, or Toggle).
    :param parent: The parent object.
    :param text: The text content of the item.
    :param children: List of child blocks (optional).
    :return: A new item block object of the specified type.
    """
    return _create_item(
        item_type, parent, "default", [create_basic_rich_text(text)], children
    )


def create_basic_bulleted_list_item(
    parent: Parent, text: str, children: list[Block] = None
) -> BulletedListItem:
    """
    Factory method to create a basic BulletedListItem object.

    :param parent: The parent object.
    :param text: The text content of the bulleted list item.
    :param children: List of child blocks (optional).
    :return: A new BulletedListItem object.
    """
    return _create_basic_item(BulletedListItem, parent, text, children)


def create_basic_numbered_list_item(
    parent: Parent, text: str, children: list[Block] = None
) -> NumberedListItem:
    """
    Factory method to create a basic NumberedListItem object.

    :param parent: The parent object.
    :param text: The text content of the numbered list item.
    :param children: List of child blocks (optional).
    :return: A new NumberedListItem object.
    """
    return _create_basic_item(NumberedListItem, parent, text, children)


def create_basic_quote(
    parent: Parent, text: str, children: list[Block] = None
) -> Quote:
    """
    Factory method to create a basic Quote object.

    :param parent: The parent object.
    :param text: The text content of the quote.
    :param children: List of child blocks (optional).
    :return: A new Quote object.
    """
    return _create_basic_item(Quote, parent, text, children)


def create_basic_toggle(
    parent: Parent, text: str, children: list[Block] = None
) -> Toggle:
    """
    Factory method to create a basic Toggle object.

    :param parent: The parent object.
    :param text: The text content of the toggle.
    :param children: List of child blocks (optional).
    :return: A new Toggle object.
    """
    return _create_basic_item(Toggle, parent, text, children)


def create_basic_to_do(
    parent: Parent,
    text: str,
    checked: Optional[bool] = None,
    children: list[Block] = None,
) -> ToDo:
    """
    Factory method to create a basic ToDo object.

    :param parent: The parent object.
    :param text: The text content of the to-do item.
    :param checked: Whether the to-do item is checked (optional).
    :param children: List of child blocks (optional).
    :return: A new ToDo object.
    """
    return create_to_do(
        parent, "default", [create_basic_rich_text(text)], checked, children
    )


__all__ = [
    "create_bulleted_list_item",
    "create_numbered_list_item",
    "create_basic_paragraph",
    "create_paragraph",
    "create_quote",
    "create_toggle",
    "create_basic_bulleted_list_item",
    "create_basic_numbered_list_item",
    "create_basic_quote",
    "create_basic_toggle",
    "create_basic_to_do",
    "create_to_do",
]
