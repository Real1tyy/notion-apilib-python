# Standard Library
from typing import Optional

from pydantic import BaseModel, Field

from RichText import RichText
# Third Party
from block import Block


class Items(BaseModel):
    """
    Base attributes for list items and other block types.

    :param color: Color of the item text.
    :param children: List of child blocks (default is an empty list).
    :param rich_text: List of rich text elements.
    """
    color: str
    children: list[Block] = Field(default_factory=list, exclude=True)
    rich_text: list[RichText]


class BulletedListItem(Block):
    """
    Bulleted list item block.

    :param bulleted_list_item: Attributes for the bulleted list item.
    """
    bulleted_list_item: Items


class NumberedListItem(Block):
    """
    Numbered list item block.

    :param numbered_list_item: Attributes for the numbered list item.
    """
    numbered_list_item: Items


class Paragraph(Block):
    """
    Paragraph block.

    :param paragraph: Attributes for the paragraph.
    """
    paragraph: Items


class Quote(Block):
    """
    Quote block.

    :param quote: Attributes for the quote.
    """
    quote: Items


class TodoAttributes(Items):
    """
    Attributes for todo items.

    :param checked: Whether the todo item is checked.
    """
    checked: Optional[bool]


class ToDo(Block):
    """
    To-do block.

    :param to_do: Attributes for the to-do item.
    """
    to_do: TodoAttributes


class Toggle(Block):
    """
    Toggle block.

    :param toggle: Attributes for the toggle item.
    """
    toggle: Items
