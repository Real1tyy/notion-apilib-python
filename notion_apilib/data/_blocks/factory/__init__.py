"""
This package contains factory methods for creating various block objects used in the Notion API. These factory methods ensure that
the block objects are instantiated with the necessary attributes and validations, streamlining the process of creating consistent and correctly structured objects.

Purpose:
    - Provide factory methods to create instances of different block objects for the Notion API.
    - Encapsulate the creation logic for block objects, ensuring that they are created with
      all required attributes and adhere to the expected structure.
    - Simplify the instantiation process for developers by offering pre-defined methods to create
      complex block objects with minimal effort.

Implementation Details:
    - The package includes factory methods for various block types, including child blocks, headings,
      list items, other types of blocks (e.g., callouts, synced blocks), tables, code blocks,
      equations, link previews, and resource blocks (e.g., files, images, videos, PDFs).
    - Each factory method is designed to instantiate and return a block object with default
      values and any necessary validations.
    - The factory methods leverage Pydantic models defined in the `_data` package to ensure data
      integrity and consistency.

Factory Methods:
    - create_child_page
    - create_child_database
    - create_heading1
    - create_heading2
    - create_heading3
    - create_basic_heading1
    - create_basic_heading2
    - create_basic_heading3
    - create_bulleted_list_item
    - create_numbered_list_item
    - create_to_do
    - create_quote
    - create_toggle
    - create_paragraph
    - create_basic_bulleted_list_item
    - create_basic_numbered_list_item
    - create_basic_quote
    - create_basic_toggle
    - create_basic_to_do
    - create_basic_paragraph
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
    This package is intended for use by developers to simplify the creation of Notion block objects.
    It provides factory methods that ensure all block objects are created consistently and correctly.
"""

from ._children.child_ import create_child_database, create_child_page
from ._children.heading_ import (
    create_basic_heading1,
    create_basic_heading2,
    create_basic_heading3,
    create_heading1,
    create_heading2,
    create_heading3,
)
from ._children.items_ import (
    create_basic_bulleted_list_item,
    create_basic_numbered_list_item,
    create_basic_paragraph,
    create_basic_quote,
    create_basic_to_do,
    create_basic_toggle,
    create_bulleted_list_item,
    create_numbered_list_item,
    create_paragraph,
    create_quote,
    create_to_do,
    create_toggle,
)
from ._children.other_ import create_callout, create_synced_block
from ._children.tables_ import create_column, create_table, create_table_of_contents, create_table_row
from .code_ import create_code
from .equation_ import create_equation
from .link_ import create_bookmark, create_embed, create_link_preview
from .other_ import create_breadcrumb, create_column_list, create_divider, create_unsupported
from .resources_ import create_file, create_image, create_pdf, create_video

__all__ = [
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
]
