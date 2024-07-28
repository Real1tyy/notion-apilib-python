from pipes import Template

from Block import Block
from Child import ChildDatabase, ChildPage
from Heading import Heading1, Heading2, Heading3
from Items import BulletedListItem, NumberedListItem, Paragraph, Quote, ToDo, Toggle
from LinkPreview import LinkPreview
from Resources import FileObject
from Resources import Image, Pdf, Video
from SyncedBlock import SyncedBlock
from Tables import Table
from Tables import TableOfContents, TableRow, Column
from block_types.concrete.Bookmark import Bookmark
from block_types.concrete.Code import Code
from block_types.concrete.Embed import Embed
from block_types.concrete.Equation import Equation
from block_types.concrete.Mention import Mention
from block_types.concrete.Other import Divider, Breadcrumb, ColumnList, Unsupported
from block_types.concrete.nestable.Callout import Callout
from custom_types import json_


class BlockTypeFactory:
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
        "template": Template,
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

    @staticmethod
    def create_concrete_type_dto(data: json_) -> Block:
        block_type = data["type"]
        return BlockTypeFactory.BLOCK_TYPE_MAP[block_type](**data)
