# Standard Library
from typing import Optional

from pydantic import BaseModel, Field

# Third Party
from _blocks.block import Block, BlockType
from structures import RichText


class Items(BaseModel):
    """
    Base attributes for list items and other _blocks types.

    :param color: Color of the item text.
    :param children: List of child _blocks (default is an empty list).
    :param rich_text: List of rich text elements.
    """
    color: str
    children: list[Block] = Field(default_factory=list, exclude=True)
    rich_text: list[RichText]


class BulletedListItem(Block):
    """
    Bulleted list item _blocks.

    :param bulleted_list_item: Attributes for the bulleted list item.
    """
    bulleted_list_item: Items

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.BULLETED_LIST_ITEM


class NumberedListItem(Block):
    """
    Numbered list item _blocks.

    :param numbered_list_item: Attributes for the numbered list item.
    """
    numbered_list_item: Items

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.NUMBERED_LIST_ITEM


class Paragraph(Block):
    """
    Paragraph _blocks.

    :param paragraph: Attributes for the paragraph.
    """
    paragraph: Items

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.PARAGRAPH


class Quote(Block):
    """
    Quote _blocks.

    :param quote: Attributes for the quote.
    """
    quote: Items

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.QUOTE


class ToDoAttributes(Items):
    """
    Attributes for todo items.

    :param checked: Whether the todo item is checked.
    """
    checked: Optional[bool]


class ToDo(Block):
    """
    To-do _blocks.

    :param to_do: Attributes for the to-do item.
    """
    to_do: ToDoAttributes

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.TO_DO


class Toggle(Block):
    """
    Toggle _blocks.

    :param toggle: Attributes for the toggle item.
    """
    toggle: Items

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.TOGGLE


__all__ = ['BulletedListItem', 'NumberedListItem', 'Paragraph', 'Quote', 'ToDo', 'Toggle']
