"""
The `_data` package contains the Pydantic data models for various block objects used in the Notion API.
These data models define the structure and validation rules for different types of _blocks, ensuring
data integrity and consistency when interacting with the Notion API.

Purpose:
    - Define the data models for Notion _blocks using Pydantic.
    - Enforce validation rules to ensure block objects adhere to the expected structure and data types.
    - Serve as the foundational layer for block objects, supporting the higher-level API provided by the main package.

Implementation Details:
    - The package includes data models for various block types, including child _blocks, headings, list items,
      other types of _blocks (e.g., callouts, synced _blocks), tables, code _blocks, equations, link previews,
      and resource _blocks (e.g., files, images, videos, PDFs).
    - Each data model is implemented as a Pydantic model, providing automatic validation and serialization.
    - The data models define the attributes and types for each block, ensuring that all required fields are
      present and correctly typed.

Data Models:
    - Models for child pages and databases.
    - Models for heading _blocks (Heading1, Heading2, Heading3).
    - Models for list items (bulleted list items, numbered list items, paragraphs, quotes, to-do items, toggles).
    - Models for other child _blocks (callouts, synced _blocks).
    - Models for table _blocks (tables, table rows, table of contents).
    - Models for code _blocks.
    - Models for equation _blocks.
    - Models for link previews.
    - Models for other _blocks (dividers, unsupported _blocks, column lists, breadcrumbs).
    - Models for resource _blocks (files, images, videos, PDFs).

Note:
    This package is intended for internal use within the library to define and validate the structure
    of block objects. It is not intended to be used directly by end-users.
"""
