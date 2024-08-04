# Third Party
from _data.mention import Mention
from data.Embed import Embed
from data.LinkPreview import LinkPreview
from synced import SyncedBlock

from FileObject import FileObject
from _data.code import Code
from _data.equation import Equation
from _data.link import Bookmark
from _data.other import Breadcrumb, ColumnList, Divider, Unsupported
from _data.resources import Image, Pdf, Video
from child import ChildDatabase, ChildPage
from custom_types import json_
from heading import Heading1, Heading2, Heading3
from items import BulletedListItem, NumberedListItem, Paragraph, Quote, ToDo, Toggle
from other import Callout
from tables import Column, Table, TableOfContents, TableRow

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


def create_concrete_block_type(data: json_):
    block_type = data["type"]
    return BLOCK_TYPE_MAP[block_type](**data)
