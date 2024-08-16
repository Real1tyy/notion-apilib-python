# Standard Library
from typing import Any

# First Party
from .data import *
from notion_api.data.structures import Mention

BLOCK_TYPE_MAP = {
    "bookmark": Bookmark,
    "breadcrumb": Breadcrumb,
    "code": Code,
    "column_list": ColumnList,
    "divider": Divider,
    "embed": Embed,
    "equation": Equation,
    "file": File,
    "image": Image,
    "link_preview": LinkPreview,
    "pdf": Pdf,
    "unsupported": Unsupported,
    "video": Video,
    "bulleted_list_item": BulletedListItem,
    "callout": Callout,
    "child_database": ChildDatabase,
    "child_page": ChildPage,
    "column": Column,
    "numbered_list_item": NumberedListItem,
    "paragraph": Paragraph,
    "quote": Quote,
    "synced_block": SyncedBlock,
    "to_do": ToDo,
    "toggle": Toggle,
    "heading_1": Heading1,
    "heading_2": Heading2,
    "heading_3": Heading3,
    "table": Table,
    "table_of_contents": TableOfContents,
    "table_row": TableRow,
    "mention": Mention,
}


def deserialize_block(data: dict[str, Any]):
    """
    Create an instance of a concrete block type based on the given json format data.

    :param data: The data used to create the block, including the block type.
    :type data: dict
    :return: An instance of the concrete block type.
    :rtype: Block
    """
    block_type = data["type"]
    return BLOCK_TYPE_MAP[block_type](**data)


__all__ = [
    "deserialize_block",
]
