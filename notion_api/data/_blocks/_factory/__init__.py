"""
The `_factory` package contains the implementation details for factory methods that create various
block objects used in the Notion API. These factory methods ensure that block objects are instantiated
with the necessary attributes and validations, streamlining the process of creating consistent and
correctly structured objects.

Purpose:
    - Provide factory methods to create instances of different block objects for the Notion API.
    - Encapsulate the creation logic for block objects, ensuring they are created with all required
      attributes and adhere to the expected structure.
    - Simplify the instantiation process for developers by offering pre-defined methods to create
      complex block objects with minimal effort.

Implementation Details:
    - The package includes factory methods for various block types, including child _blocks, headings,
      list items, other types of _blocks (e.g., callouts, synced _blocks), tables, code _blocks, equations,
      link previews, and resource _blocks (e.g., files, images, videos, PDFs).
    - Each factory method is designed to instantiate and return a block object with default values
      and any necessary validations.
    - The factory methods leverage Pydantic models defined in the `_data` package to ensure data
      integrity and consistency.

Factory Methods:
    - Methods to create child pages and databases.
    - Methods to create heading _blocks (Heading1, Heading2, Heading3).
    - Methods to create list items (bulleted list items, numbered list items, to-do items, quotes, toggles, paragraphs).
    - Methods to create other child _blocks (callouts, synced _blocks).
    - Methods to create table _blocks (tables, table rows, columns, table of contents).
    - Methods to create code _blocks.
    - Methods to create equation _blocks.
    - Methods to create link previews, embeds, and bookmarks.
    - Methods to create other _blocks (dividers, breadcrumbs, unsupported _blocks, column lists).
    - Methods to create resource _blocks (PDFs, videos, files, images).

Note:
    This package is intended for internal use within the library to support the creation
    of block objects. It is not intended to be used directly by end-users.
"""
