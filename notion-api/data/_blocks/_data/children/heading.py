from pydantic import BaseModel

from block import Block
from structures import RichText


class HeadingsAttributes(BaseModel):
    """
    Attributes for heading _blocks.

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
    Heading 2 _blocks.

    :param heading_2: Attributes for the heading 2 _blocks.
    """
    heading_2: HeadingsAttributes


class Heading3(Block):
    """
    Heading 3 _blocks.

    :param heading_3: Attributes for the heading 3 _blocks.
    """
    heading_3: HeadingsAttributes
