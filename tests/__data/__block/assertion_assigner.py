# Standard Library
from typing import Callable, Type

# First Party
from notion_api.data.blocks import (
    Block,
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
)

from .__children.test_child import assert_child_data_is_correct
from .__children.test_heading import assert_heading_data_is_correct
from .__children.test_items import assert_item_data_is_correct, assert_todo_data_is_correct
from .__children.test_other import assert_callout_data_is_correct, assert_synced_block_data_is_correct
from .__children.test_tables import (
    assert_column_data_is_correct,
    assert_table_data_is_correct,
    assert_table_of_contents_data_is_correct,
    assert_table_row_data_is_correct,
)
from .test_code import assert_code_data_is_correct
from .test_equation import assert_equation_data_is_correct
from .test_link import assert_bookmark_data_is_correct, assert_embed_or_link_preview_data_is_correct
from .test_other import assert_empty_block_data_is_correct
from .test_resources import assert_file_data_is_correct, assert_resources_data_is_correct

ASSERTIONS_MAP = {
    ChildPage: assert_child_data_is_correct,
    ChildDatabase: assert_child_data_is_correct,
    Heading1: assert_heading_data_is_correct,
    Heading2: assert_heading_data_is_correct,
    Heading3: assert_heading_data_is_correct,
    BulletedListItem: assert_item_data_is_correct,
    NumberedListItem: assert_item_data_is_correct,
    Paragraph: assert_item_data_is_correct,
    Quote: assert_item_data_is_correct,
    Toggle: assert_item_data_is_correct,
    ToDo: assert_todo_data_is_correct,
    Callout: assert_callout_data_is_correct,
    SyncedBlock: assert_synced_block_data_is_correct,
    Table: assert_table_data_is_correct,
    TableRow: assert_table_row_data_is_correct,
    TableOfContents: assert_table_of_contents_data_is_correct,
    Column: assert_column_data_is_correct,
    Code: assert_code_data_is_correct,
    Equation: assert_equation_data_is_correct,
    Bookmark: assert_bookmark_data_is_correct,
    Embed: assert_embed_or_link_preview_data_is_correct,
    LinkPreview: assert_embed_or_link_preview_data_is_correct,
    File: assert_file_data_is_correct,
    Image: assert_resources_data_is_correct,
    Pdf: assert_resources_data_is_correct,
    Video: assert_resources_data_is_correct,
    Divider: assert_empty_block_data_is_correct,
    Breadcrumb: assert_empty_block_data_is_correct,
    ColumnList: assert_empty_block_data_is_correct,
    Unsupported: assert_empty_block_data_is_correct,
}


def get_assertion_function(block_class: Type[Block]) -> Callable:
    """
    Retrieve the assertion function for a given block class.

    Parameters:
        block_class (type): The class of the block.

    Returns:
        function: The corresponding assertion function.
    """
    return ASSERTIONS_MAP.get(block_class)
