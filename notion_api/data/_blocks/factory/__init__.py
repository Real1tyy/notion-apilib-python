"""
This package contains factory methods
for creating various block objects used in the Notion API. These factory methods ensure that
the block objects are instantiated with the necessary attributes and validations, streamlining
the process of creating consistent and correctly structured objects.

Purpose:
    - Provide factory methods to create instances of different block objects for the Notion API.
    - Encapsulate the creation logic for block objects, ensuring that they are created with
      all required attributes and adhere to the expected structure.
    - Simplify the instantiation process for developers by offering pre-defined methods to create
      complex block objects with minimal effort.

Implementation Details:
    - The package includes factory methods for various block types, including child _blocks, headings,
      list items, other types of _blocks (e.g., callouts, synced _blocks), tables, code _blocks,
      equations, link previews, and resource _blocks (e.g., files, images, videos, PDFs).
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
    This package is intended for use by developers to simplify the creation of Notion block objects.
    It provides factory methods that ensure all block objects are created consistently and correctly.
"""
from notion_api.data._blocks._factory.children.heading import *
from notion_api.data._blocks._factory.children.child import *
from notion_api.data._blocks._factory.children.items import *
from notion_api.data._blocks._factory.children.other import *
from notion_api.data._blocks._factory.children.tables import *
from notion_api.data._blocks._factory.code import *
from notion_api.data._blocks._factory.equation import *
from notion_api.data._blocks._factory.link import *
from notion_api.data._blocks._factory.other import *
from notion_api.data._blocks._factory.resources import *

from notion_api.data._blocks._factory.children.heading import __all__ as heading_all
from notion_api.data._blocks._factory.children.child import __all__ as child_all
from notion_api.data._blocks._factory.children.items import __all__ as items_all
from notion_api.data._blocks._factory.children.other import __all__ as other_all
from notion_api.data._blocks._factory.children.tables import __all__ as tables_all
from notion_api.data._blocks._factory.code import __all__ as code_all
from notion_api.data._blocks._factory.equation import __all__ as equation_all
from notion_api.data._blocks._factory.link import __all__ as link_all
from notion_api.data._blocks._factory.other import __all__ as other_basic_all
from notion_api.data._blocks._factory.resources import __all__ as resources_all

__all__ = (heading_all + child_all + items_all + other_all + tables_all + code_all + equation_all +
           link_all + other_basic_all + resources_all)
