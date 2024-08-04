"""
The `_data.children` package contains Pydantic data models for _blocks that can have children in the Notion API.
This package is used to differentiate between _blocks that can have children and those that cannot.

Purpose:
    - Define the data models for Notion _blocks that can have children using Pydantic.
    - Ensure data integrity and consistency for _blocks that support child _blocks.

Implementation Details:
    - The package includes data models for various block types that can have children, such as child pages,
      child databases, headings, list items, and other child-supporting _blocks.

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

Note:
    This package is intended for internal use within the library to support the structure
    and validation of _blocks that can have children. It is not intended to be used directly by end-users.
"""
