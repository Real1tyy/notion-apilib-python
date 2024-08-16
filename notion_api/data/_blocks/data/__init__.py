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

# First Party
from notion_api.data._blocks._data.children.child import *
from notion_api.data._blocks._data.children.child import __all__ as child_all
from notion_api.data._blocks._data.children.heading import *
from notion_api.data._blocks._data.children.heading import __all__ as heading_all
from notion_api.data._blocks._data.children.items import *
from notion_api.data._blocks._data.children.items import __all__ as items_all
from notion_api.data._blocks._data.children.other import *
from notion_api.data._blocks._data.children.other import __all__ as other_all
from notion_api.data._blocks._data.children.tables import *
from notion_api.data._blocks._data.children.tables import __all__ as tables_all
from notion_api.data._blocks._data.code import *
from notion_api.data._blocks._data.code import __all__ as code_all
from notion_api.data._blocks._data.equation import *
from notion_api.data._blocks._data.equation import __all__ as equation_all
from notion_api.data._blocks._data.link import *
from notion_api.data._blocks._data.link import __all__ as link_all
from notion_api.data._blocks._data.other import *
from notion_api.data._blocks._data.other import __all__ as other_basic_all
from notion_api.data._blocks._data.resources import *
from notion_api.data._blocks._data.resources import __all__ as resources_all
from notion_api.data._blocks.block import Block

__all__ = (child_all + heading_all + items_all + other_all + tables_all + code_all + equation_all +
           link_all + other_basic_all + resources_all)
