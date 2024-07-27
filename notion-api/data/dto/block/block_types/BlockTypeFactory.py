from Block import Block
from custom_types import json_


class BlockTypeFactory:
    from block_types.concrete.Bookmark import Bookmark
    from block_types.concrete.Breadcrumb import Breadcrumb
    from block_types.concrete.Code import Code
    from block_types.concrete.ColumnList import ColumnList
    from block_types.concrete.Divider import Divider
    from block_types.concrete.Embed import Embed
    from block_types.concrete.Equation import Equation
    from block_types.concrete.File import File
    from block_types.concrete.Image import Image
    from block_types.concrete.LinkPreview import LinkPreview
    from block_types.concrete.Pdf import Pdf
    from block_types.concrete.Unsupported import Unsupported
    from block_types.concrete.Video import Video
    from block_types.concrete.Mention import Mention
    from block_types.concrete.nestable.BulletedListItem import BulletedListItem
    from block_types.concrete.nestable.Callout import Callout
    from block_types.concrete.nestable.ChildDatabase import ChildDatabase
    from block_types.concrete.nestable.ChildPage import ChildPage
    from block_types.concrete.nestable.Column import Column
    from block_types.concrete.nestable.NumberedListItem import NumberedListItem
    from block_types.concrete.nestable.Paragraph import Paragraph
    from block_types.concrete.nestable.Quote import Quote
    from block_types.concrete.nestable.SyncedBlock import SyncedBlock
    from block_types.concrete.nestable.Template import Template
    from block_types.concrete.nestable.ToDo import ToDo
    from block_types.concrete.nestable.Toggle import Toggle
    from block_types.concrete.nestable.headings.Heading1 import Heading1DTO
    from block_types.concrete.nestable.headings.Heading2 import Heading2DTO
    from block_types.concrete.nestable.headings.Heading3 import Heading3DTO
    from block_types.concrete.nestable.tables.Table import Table
    from block_types.concrete.nestable.tables.TableOfContents import TableOfContents
    from block_types.concrete.nestable.tables.TableRow import TableRow
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
        "template": Template,
        "to_do": ToDo,
        "toggle": Toggle,
        "heading_1": Heading1DTO,
        "heading_2": Heading2DTO,
        "heading_3": Heading3DTO,
        "table": Table,
        "table_of_contents": TableOfContents,
        "table_row": TableRow,
        "mention": Mention
    }

    @staticmethod
    def create_concrete_type_dto(data: json_) -> Block:
        block_type = data["type"]
        res = BlockTypeFactory.BLOCK_TYPE_MAP[block_type](**data)
        return res
