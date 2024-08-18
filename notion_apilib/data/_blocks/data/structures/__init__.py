"""
This module exposes attributes for various Notion block types, providing validation and structure
for different block components in the Notion API. These attributes are defined using Pydantic models
and ensure that block objects adhere to the expected structure and data types.

The attributes exposed in this module are:

- ChildAttributes
- HeadingsAttributes
- Items
- ToDoAttributes
- CalloutAttributes
- SyncedBlockAttributes
- TableAttributes
- TableRowAttributes
- TableOfContentsAttributes
- CodeAttributes
- EquationAttributes
- LinkPreviewAttributes
- EmbedAttributes
- BookmarkAttributes
"""

from .._children.child_ import ChildAttributes
from .._children.heading_ import HeadingsAttributes
from .._children.items_ import Items, ToDoAttributes
from .._children.other_ import CalloutAttributes, SyncedBlockAttributes, SyncedFrom
from .._children.tables_ import (
    TableAttributes,
    TableOfContentsAttributes,
    TableRowAttributes,
)
from ..code_ import CodeAttributes
from ..equation_ import EquationAttributes
from ..link_ import BookmarkAttributes, EmbedAttributes, LinkPreviewAttributes

__all__ = [
    "ChildAttributes",
    "HeadingsAttributes",
    "Items",
    "ToDoAttributes",
    "CalloutAttributes",
    "SyncedBlockAttributes",
    "SyncedFrom",
    "TableAttributes",
    "TableRowAttributes",
    "TableOfContentsAttributes",
    "CodeAttributes",
    "EquationAttributes",
    "LinkPreviewAttributes",
    "EmbedAttributes",
    "BookmarkAttributes",
]
