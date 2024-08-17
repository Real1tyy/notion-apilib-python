"""
This package contains all the Pydantic models
for validating various types of _blocks in the Notion API. Each block type has its own data model
that defines the structure and validation rules, ensuring data integrity and consistency when
interacting with the Notion API.

Purpose:
    - Define the data models for Notion _blocks using Pydantic.
    - Enforce validation rules to ensure block objects adhere to the expected structure and data types.
    - Provide a user-friendly interface for creating and interacting with block objects in the Notion API.

Implementation Details:
    - The package includes data models for various block types, including child _blocks, headings,
      list items, other types of _blocks (e.g., callouts, synced _blocks), tables, code _blocks,
      equations, link previews, and resource _blocks (e.g., files, images, videos, PDFs).
    - Each data model is implemented as a Pydantic model, providing automatic validation and serialization.
    - The data models define the attributes and types for each block, ensuring that all required
      fields are present and correctly typed.

Data Models:
    - ChildDatabase
    - ChildPage
    - Heading1
    - Heading2
    - Heading3
    - BulletedListItem
    - NumberedListItem
    - Paragraph
    - Quote
    - TodoAttributes
    - ToDo
    - Toggle
    - Callout
    - SyncedBlock
    - Table
    - TableRow
    - TableOfContents
    - Column
    - Code
    - Equation
    - LinkPreview
    - Embed
    - Bookmark
    - Divider
    - Unsupported
    - ColumnList
    - Breadcrumb
    - File
    - Image
    - Video
    - Pdf
    - structures - module that contains all the lower level structures pydantic models used for validation.

Note:
    This package is intended for use by end-users to create and interact with Notion block objects.
    It provides a user-friendly interface and ensures that all block objects are validated and structured
    correctly.
"""

# First Party
import notion_apilib.data._blocks.data.structures as block_structures

from ._children.child_ import ChildDatabase, ChildPage
from ._children.heading_ import Heading1, Heading2, Heading3
from ._children.items_ import BulletedListItem, NumberedListItem, Paragraph, Quote, ToDo, Toggle
from ._children.other_ import Callout, SyncedBlock
from ._children.tables_ import Column, Table, TableOfContents, TableRow
from .code_ import Code
from .equation_ import Equation
from .link_ import Bookmark, Embed, LinkPreview
from .other_ import Breadcrumb, ColumnList, Divider, Unsupported
from .resources_ import File, Image, Pdf, Video

__all__ = [
    "ChildDatabase",
    "ChildPage",
    "Heading1",
    "Heading2",
    "Heading3",
    "BulletedListItem",
    "NumberedListItem",
    "Paragraph",
    "Quote",
    "ToDo",
    "Toggle",
    "Callout",
    "SyncedBlock",
    "Table",
    "TableRow",
    "TableOfContents",
    "Column",
    "Code",
    "Equation",
    "LinkPreview",
    "Embed",
    "Bookmark",
    "Divider",
    "Unsupported",
    "Breadcrumb",
    "ColumnList",
    "File",
    "Image",
    "Video",
    "Pdf",
    "block_structures",
]
