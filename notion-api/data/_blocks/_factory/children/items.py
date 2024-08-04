from typing import Type, Optional

from _data.Parent import Parent
from _data.RichText import RichText
from block import Block, _create_block
from items import Items, BulletedListItem, NumberedListItem, Paragraph, Quote, TodoAttributes, ToDo, Toggle
from type import BlockType


def _create_item_block(
        block_class: Type[Block], block_type: BlockType, parent: Parent,
        color: str, rich_text: list[RichText], children: Optional[list[Block]] = None) -> Type[Block]:
    """
    Helper function to create an item _blocks object.

    :param block_class: The class of the _blocks to create.
    :param block_type: The type of the _blocks.
    :param parent: The parent object.
    :param color: The color of the item text.
    :param rich_text: The rich text content of the item.
    :param children: List of child _blocks (optional).
    :return: A new _blocks object.
    """
    return _create_block(
        block_class,
        parent=parent,
        block_type=block_type,
        **{block_type.value.lower(): Items(
            color=color,
            rich_text=rich_text,
            children=children if children else []
        )},
        children=children
    )


def create_bulleted_list_item(
        parent: Parent, color: str, rich_text: list[RichText], children: list[Block] = None) -> BulletedListItem:
    """
    Factory method to create a BulletedListItem object.

    :param parent: The parent object.
    :param color: The color of the item text.
    :param rich_text: The rich text content of the item.
    :param children: List of child _blocks (optional).
    :return: A new BulletedListItem object.
    """
    return _create_item_block(
        BulletedListItem,
        BlockType.BULLETED_LIST_ITEM,
        parent,
        color,
        rich_text,
        children
    )


def create_numbered_list_item(
        parent: Parent, color: str, rich_text: list[RichText], children: list[Block] = None) -> NumberedListItem:
    """
    Factory method to create a NumberedListItem object.

    :param parent: The parent object.
    :param color: The color of the item text.
    :param rich_text: The rich text content of the item.
    :param children: List of child _blocks (optional).
    :return: A new NumberedListItem object.
    """
    return _create_item_block(
        NumberedListItem,
        BlockType.NUMBERED_LIST_ITEM,
        parent,
        color,
        rich_text,
        children
    )


def create_paragraph(
        parent: Parent, color: str, rich_text: list[RichText], children: list[Block] = None) -> Paragraph:
    """
    Factory method to create a Paragraph object.

    :param parent: The parent object.
    :param color: The color of the paragraph text.
    :param rich_text: The rich text content of the paragraph.
    :param children: List of child _blocks (optional).
    :return: A new Paragraph object.
    """
    return _create_item_block(
        Paragraph,
        BlockType.PARAGRAPH,
        parent,
        color,
        rich_text,
        children
    )


def create_quote(
        parent: Parent, color: str, rich_text: list[RichText], children: list[Block] = None) -> Quote:
    """
    Factory method to create a Quote object.

    :param parent: The parent object.
    :param color: The color of the quote text.
    :param rich_text: The rich text content of the quote.
    :param children: List of child _blocks (optional).
    :return: A new Quote object.
    """
    return _create_item_block(
        Quote,
        BlockType.QUOTE,
        parent,
        color,
        rich_text,
        children
    )


def create_to_do(
        parent: Parent, color: str, rich_text: list[RichText], checked: Optional[bool] = None,
        children: list[Block] = None) -> ToDo:
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
        block_type=BlockType.TO_DO,
        to_do=TodoAttributes(
            color=color,
            rich_text=rich_text,
            checked=checked,
            children=children if children else []
        ),
        children=children
    )


def create_toggle(
        parent: Parent, color: str, rich_text: list[RichText], children: list[Block] = None) -> Toggle:
    """
    Factory method to create a Toggle object.

    :param parent: The parent object.
    :param color: The color of the toggle text.
    :param rich_text: The rich text content of the toggle.
    :param children: List of child _blocks (optional).
    :return: A new Toggle object.
    """
    return _create_item_block(
        Toggle,
        BlockType.TOGGLE,
        parent,
        color,
        rich_text,
        children
    )
