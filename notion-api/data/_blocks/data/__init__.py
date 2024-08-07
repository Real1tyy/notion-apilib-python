"""
This package, called `data`, is part of the `_blocks` package and contains all the Pydantic models
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

Modules Included:
    - children.child: Data models for child pages and databases.
    - children.heading: Data models for headings (Heading1, Heading2, Heading3).
    - children.items: Data models for list items (BulletedListItem, NumberedListItem, Paragraph, Quote, ToDo, Toggle).
    - children.other: Data models for other child _blocks (Callout, SyncedBlock).
    - children.tables: Data models for tables (Table, TableRow, TableOfContents).
    - code: Data model for code _blocks.
    - equation: Data model for equation _blocks.
    - link: Data model for link previews.
    - other: Data models for other _blocks (Divider, Unsupported, ColumnList, Breadcrumb).
    - resources: Data models for resource _blocks (File, Image, Video, Pdf).

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
    - Code
    - Equation
    - LinkPreview
    - Divider
    - Unsupported
    - ColumnList
    - Breadcrumb
    - File
    - Image
    - Video
    - Pdf

Note:
    This package is intended for use by end-users to create and interact with Notion block objects.
    It provides a user-friendly interface and ensures that all block objects are validated and structured
    correctly.
"""

from _blocks._data.children.child import ChildDatabase, ChildPage, ChildAttributes
from _blocks._data.children.heading import Heading1, Heading2, Heading3, HeadingsAttributes
from _blocks._data.children.items import (BulletedListItem, NumberedListItem, Paragraph, Quote, TodoAttributes, ToDo,
                                          Toggle, Items)
from _blocks._data.children.other import Callout, SyncedBlock, SyncedBlockAttributes, SyncedFrom, CalloutAttributes
from _blocks._data.children.tables import (Table, TableRow, TableOfContents, Column, TableRowAttributes,
                                           TableAttributes, TableOfContentsAttributes)
from _blocks._data.code import Code, CodeAttributes
from _blocks._data.equation import Equation, EquationAttributes
from _blocks._data.link import LinkPreview, Bookmark, Embed, BookmarkAttributes, EmbedAttributes, LinkPreviewAttributes
from _blocks._data.other import Divider, Unsupported, ColumnList, Breadcrumb
from _blocks._data.resources import File, Image, Video, Pdf

__all__ = [
    'ChildDatabase', 'ChildPage', 'ChildAttributes',
    'Heading1', 'Heading2', 'Heading3', 'HeadingsAttributes',
    'BulletedListItem', 'NumberedListItem', 'Paragraph', 'Quote', 'TodoAttributes', 'ToDo', 'Toggle', 'Items',
    'Callout', 'SyncedBlock', 'CalloutAttributes', 'SyncedBlockAttributes', 'SyncedFrom',
    'Table', 'TableRow', 'TableOfContents', 'Column', 'TableRowAttributes', 'TableAttributes',
    'TableOfContentsAttributes',
    'Code', 'CodeAttributes',
    'Equation', 'EquationAttributes',
    'LinkPreview', 'Bookmark', 'Embed', 'BookmarkAttributes', 'EmbedAttributes', 'LinkPreviewAttributes',
    'Divider', 'Unsupported', 'ColumnList', 'Breadcrumb',
    'File', 'Image', 'Video', 'Pdf'
]
