from Block import Block
from Bookmark import Bookmark
from Callout import Callout
from Child import ChildDatabase, ChildPage
from Code import Code
from Embed import Embed
from Equation import Equation
from FileObject import FileObject
from Heading import Heading1, Heading2, Heading3
from Items import BulletedListItem, NumberedListItem, Paragraph, Quote, ToDo, Toggle
from LinkPreview import LinkPreview
from Mention import Mention
from Other import Divider, Breadcrumb, ColumnList, Unsupported
from Resources import Image, Pdf, Video
from SyncedBlock import SyncedBlock
from Tables import Table
from Tables import TableOfContents, TableRow, Column
from custom_types import json_

BLOCK_TYPE_MAP = {
    "bookmark": Bookmark,
    "breadcrumb": Breadcrumb,
    "code": Code,
    "column_list": ColumnList,
    "divider": Divider,
    "embed": Embed,
    "equation": Equation,
    "file": FileObject,
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
    "mention": Mention
}


def create_concrete_block_type(data: json_) -> Block:
    block_type = data["type"]
    return BLOCK_TYPE_MAP[block_type](**data)
