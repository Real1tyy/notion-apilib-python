"""
The `_blocks` package contains the internal implementation details for handling blocks in the Notion API.
This includes both the Pydantic models for validating block objects and the factory methods for creating them.
The package ensures data integrity and consistency when interacting with the Notion API by providing validated
data models and streamlined creation methods.

Purpose:
    - Define and validate data models for Notion blocks using Pydantic.
    - Provide factory methods to create instances of block objects with the necessary attributes and validations.
    - Encapsulate the creation logic and validation rules internally to support the public interface.

Implementation Details:
    - The package includes data models and factory methods for various block types, including child blocks,
      headings, list items, other types of blocks (e.g., callouts, synced blocks), tables, code blocks,
      equations, link previews, and resource blocks (e.g., files, images, videos, PDFs).
    - Each data model is implemented as a Pydantic model, ensuring automatic validation and serialization.
    - Each factory method is designed to instantiate and return a block object with default values and necessary
      validations, leveraging the Pydantic models defined in the package.

Modules Included:
    - children.child: Data models and factory methods for child pages and databases.
    - children.heading: Data models and factory methods for headings (Heading1, Heading2, Heading3).
    - children.items: Data models and factory methods for list items (BulletedListItem, NumberedListItem, Paragraph, Quote, ToDo, Toggle).
    - children.other: Data models and factory methods for other child blocks (Callout, SyncedBlock).
    - children.tables: Data models and factory methods for tables (Table, TableRow, TableOfContents).
    - code: Data model and factory method for code blocks.
    - equation: Data model and factory method for equation blocks.
    - link: Data model and factory methods for link previews.
    - other: Data models and factory methods for other blocks (Divider, Unsupported, ColumnList, Breadcrumb).
    - resources: Data models and factory methods for resource blocks (File, Image, Video, Pdf).

Data Models and Factory Methods:
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
    - create_child_page
    - create_child_database
    - create_heading1
    - create_heading2
    - create_heading3
    - create_bulleted_list_item
    - create_numbered_list_item
    - create_to_do
    - create_quote
    - create_toggle
    - create_paragraph
    - create_synced_block
    - create_callout
    - create_table
    - create_table_row
    - create_column
    - create_table_of_contents
    - create_code
    - create_equation
    - create_link_preview
    - create_embed
    - create_bookmark
    - create_divider
    - create_breadcrumb
    - create_unsupported
    - create_column_list
    - create_pdf
    - create_video
    - create_file
    - create_image

Note:
    This package is intended for internal use within the library to support the public interface.
    It encapsulates the logic and validation rules to ensure consistent and correct creation and handling
    of Notion block objects.
"""
