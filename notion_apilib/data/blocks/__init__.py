"""
This package provides comprehensive tools for interacting with the Notion API. It contains:

1. **Pydantic Models**:
   - Data models for validating various types of blocks in the Notion API.
   - Each block type has its own data model that defines the structure and validation rules, ensuring data integrity and consistency.

2. **Factory Methods**:
   - Factory methods for creating various block objects used in the Notion API.
   - These methods simplify the creation of consistent and correctly structured block objects.

Purpose:
    - Define the data models for Notion blocks using Pydantic.
    - Enforce validation rules to ensure block objects adhere to the expected structure and data types.
    - Provide a user-friendly interface for creating and interacting with block objects in the Notion API.
    - Simplify the instantiation process for developers by offering pre-defined methods to create complex block objects with minimal effort.

Implementation Details:
    - The package includes data models and factory methods for various block types, including child blocks, headings, list items, other types of blocks (e.g., callouts, synced blocks), tables, code blocks, equations, link previews, and resource blocks (e.g., files, images, videos, PDFs).
    - Each data model and factory method ensures that all required fields are present and correctly typed.

Data Models and Factory Methods:
    - ChildDatabase, create_child_database
    - ChildPage, create_child_page
    - Heading1, create_heading1
    - Heading2, create_heading2
    - Heading3, create_heading3
    - BasicHeading1, create_basic_heading1
    - BasicHeading2, create_basic_heading2
    - BasicHeading3, create_basic_heading3
    - BulletedListItem, create_bulleted_list_item
    - NumberedListItem, create_numbered_list_item
    - ToDo, create_to_do
    - Quote, create_quote
    - Toggle, create_toggle
    - Paragraph, create_paragraph
    - BasicBulletedListItem, create_basic_bulleted_list_item
    - BasicNumberedListItem, create_basic_numbered_list_item
    - BasicQuote, create_basic_quote
    - BasicToggle, create_basic_toggle
    - BasicToDo, create_basic_to_do
    - BasicParagraph, create_basic_paragraph
    - Callout, create_callout
    - SyncedBlock, create_synced_block
    - Table, create_table
    - TableRow, create_table_row
    - Column, create_column
    - TableOfContents, create_table_of_contents
    - Code, create_code
    - Equation, create_equation
    - LinkPreview, create_link_preview
    - Embed, create_embed
    - Bookmark, create_bookmark
    - Divider, create_divider
    - Breadcrumb, create_breadcrumb
    - Unsupported, create_unsupported
    - ColumnList, create_column_list
    - File, create_file
    - Image, create_image
    - Video, create_video
    - Pdf, create_pdf

- block_structures (module containing all lower-level structures used for validation)

- deserialization function to convert json into a concrete block type:
    - deserialize_block converts JSON data into a concrete block type based on the block type specified in the JSON data.

- Generic Block class and BlockType:
    - Block
    - BlockType


Note:
    This package is intended for use by end-users to create and interact with Notion block objects.
    It provides a user-friendly interface and ensures that all block objects are validated and structured correctly.
    The additional factory methods enable the transformation of JSON payloads from the Notion API into our custom
    DSL block classes, facilitating seamless data integration.
"""

# Other
from .._blocks.block import Block, BlockType

# Importing data models
from .._blocks.data import (
    Bookmark,
    Breadcrumb,
    BulletedListItem,
    Callout,
    ChildDatabase,
    ChildPage,
    Code,
    Column,
    ColumnList,
    Divider,
    Embed,
    Equation,
    File,
    Heading1,
    Heading2,
    Heading3,
    Image,
    LinkPreview,
    NumberedListItem,
    Paragraph,
    Pdf,
    Quote,
    SyncedBlock,
    Table,
    TableOfContents,
    TableRow,
    ToDo,
    Toggle,
    Unsupported,
    Video,
    block_structures,
)
from .._blocks.factory import (
    create_basic_bulleted_list_item,
    create_basic_heading1,
    create_basic_heading2,
    create_basic_heading3,
    create_basic_numbered_list_item,
    create_basic_paragraph,
    create_basic_quote,
    create_basic_to_do,
    create_basic_toggle,
    create_bookmark,
    create_breadcrumb,
    create_bulleted_list_item,
    create_callout,
    create_child_database,
    create_child_page,
    create_code,
    create_column,
    create_column_list,
    create_divider,
    create_embed,
    create_equation,
    create_file,
    create_heading1,
    create_heading2,
    create_heading3,
    create_image,
    create_link_preview,
    create_numbered_list_item,
    create_paragraph,
    create_pdf,
    create_quote,
    create_synced_block,
    create_table,
    create_table_of_contents,
    create_table_row,
    create_to_do,
    create_toggle,
    create_unsupported,
    create_video,
)
from .._blocks.type_factory import deserialize_block

__all__ = [
    # Data Models
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
    # Factory Methods
    "create_child_page",
    "create_child_database",
    "create_heading1",
    "create_heading2",
    "create_heading3",
    "create_basic_heading1",
    "create_basic_heading2",
    "create_basic_heading3",
    "create_bulleted_list_item",
    "create_numbered_list_item",
    "create_to_do",
    "create_quote",
    "create_toggle",
    "create_paragraph",
    "create_basic_bulleted_list_item",
    "create_basic_numbered_list_item",
    "create_basic_quote",
    "create_basic_toggle",
    "create_basic_to_do",
    "create_basic_paragraph",
    "create_synced_block",
    "create_callout",
    "create_table",
    "create_table_row",
    "create_column",
    "create_table_of_contents",
    "create_code",
    "create_equation",
    "create_link_preview",
    "create_embed",
    "create_bookmark",
    "create_divider",
    "create_breadcrumb",
    "create_unsupported",
    "create_column_list",
    "create_pdf",
    "create_video",
    "create_file",
    "create_image",
    # Other
    "Block",
    "BlockType",
    "deserialize_block",
]
