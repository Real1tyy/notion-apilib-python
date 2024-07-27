from custom_types import json_


class BlockTypeFactory:
    from block_types.concrete.BookmarkDTO import BookmarkDTO
    from block_types.concrete.BreadcrumbDTO import BreadcrumbDTO
    from block_types.concrete.CodeDTO import CodeDTO
    from block_types.concrete.ColumnListDTO import ColumnListDTO
    from block_types.concrete.DividerDTO import DividerDTO
    from block_types.concrete.EmbedDTO import EmbedDTO
    from block_types.concrete.EquationDTO import EquationDTO
    from block_types.concrete.FileDTO import FileDTO
    from block_types.concrete.ImageDTO import ImageDTO
    from block_types.concrete.LinkPreviewDTO import LinkPreviewDTO
    from block_types.concrete.PdfDTO import PdfDTO
    from block_types.concrete.UnsupportedDTO import UnsupportedDTO
    from block_types.concrete.VideoDTO import VideoDTO
    from block_types.concrete.MentionDTO import MentionDTO
    from block_types.concrete.nestable.BulletedListItemDTO import BulletedListItemDTO
    from block_types.concrete.nestable.CalloutDTO import CalloutDTO
    from block_types.concrete.nestable.ChildDatabaseDTO import ChildDatabaseDTO
    from block_types.concrete.nestable.ChildPageDTO import ChildPageDTO
    from block_types.concrete.nestable.ColumnDTO import ColumnDTO
    from block_types.concrete.nestable.NumberedListItemDTO import NumberedListItemDTO
    from block_types.concrete.nestable.ParagraphDTO import ParagraphDTO
    from block_types.concrete.nestable.QuoteDTO import QuoteDTO
    from block_types.concrete.nestable.SyncedBlockDTO import SyncedBlockDTO
    from block_types.concrete.nestable.TemplateDTO import TemplateDTO
    from block_types.concrete.nestable.ToDoDTO import ToDoDTO
    from block_types.concrete.nestable.ToggleDTO import ToggleDTO
    from block_types.concrete.nestable.headings.Heading1DTO import Heading1DTO
    from block_types.concrete.nestable.headings.Heading2DTO import Heading2DTO
    from block_types.concrete.nestable.headings.Heading3DTO import Heading3DTO
    from block_types.concrete.nestable.tables.TableDTO import TableDTO
    from block_types.concrete.nestable.tables.TableOfContentsDTO import TableOfContentsDTO
    from block_types.concrete.nestable.tables.TableRowDTO import TableRowDTO
    BLOCK_TYPE_MAP = {
        "bookmark": BookmarkDTO,
        "breadcrumb": BreadcrumbDTO,
        "code": CodeDTO,
        "column_list": ColumnListDTO,
        "divider": DividerDTO,
        "embed": EmbedDTO,
        "equation": EquationDTO,
        "file": FileDTO,
        "image": ImageDTO,
        "link_preview": LinkPreviewDTO,
        "pdf": PdfDTO,
        "unsupported": UnsupportedDTO,
        "video": VideoDTO,
        "bulleted_list_item": BulletedListItemDTO,
        "callout": CalloutDTO,
        "child_database": ChildDatabaseDTO,
        "child_page": ChildPageDTO,
        "column": ColumnDTO,
        "numbered_list_item": NumberedListItemDTO,
        "paragraph": ParagraphDTO,
        "quote": QuoteDTO,
        "synced_block": SyncedBlockDTO,
        "template": TemplateDTO,
        "to_do": ToDoDTO,
        "toggle": ToggleDTO,
        "heading_1": Heading1DTO,
        "heading_2": Heading2DTO,
        "heading_3": Heading3DTO,
        "table": TableDTO,
        "table_of_contents": TableOfContentsDTO,
        "table_row": TableRowDTO,
        "mention": MentionDTO
    }

    @staticmethod
    def create_concrete_type_dto(data: json_):
        block_type = data["type"]
        res = BlockTypeFactory.BLOCK_TYPE_MAP[block_type](**data)
        print(type(res))
        return res
