from typing import Optional

from pydantic import BaseModel, Field

from Block import Block
from RichText import RichText


class Items(BaseModel):
    color: str
    children: list[Block] = Field(default_factory=list, exclude=True)
    rich_text: list[RichText]


class BulletedListItem(Block):
    bulleted_list_item: Items


class NumberedListItem(Block):
    numbered_list_item: Items


class Paragraph(Block):
    paragraph: Items


class Quote(Block):
    quote: Items


class TodoAttributes(Items):
    checked: Optional[bool]


class ToDo(Block):
    to_do: TodoAttributes


class Toggle(Block):
    toggle: Items
