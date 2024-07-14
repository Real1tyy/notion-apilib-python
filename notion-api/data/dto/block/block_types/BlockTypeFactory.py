# class BlockFactory:
#     from blocks.bookmark import BookmarkBlockDTO
#     from blocks.breadcrumb import BreadcrumbBlockDTO
#     from blocks.bulleted_list_item import BulletedListItemBlockDTO
#     from blocks.callout import CalloutBlockDTO
#     from blocks.child_database import ChildDatabaseBlockDTO
#     from blocks.child_page import ChildPageBlockDTO
#     from blocks.column import ColumnBlockDTO
#     from blocks.column_list import ColumnListBlockDTO
#     from blocks.divider import DividerBlockDTO
#     from blocks.embed import EmbedBlockDTO
#     from blocks.equation import EquationBlockDTO
#     from blocks.file import FileBlockDTO
#     from blocks.heading_1 import Heading1BlockDTO
#     from blocks.heading_2 import Heading2BlockDTO
#     from blocks.heading_3 import Heading3BlockDTO
#     from blocks.image import ImageBlockDTO
#     from blocks.link_preview import LinkPreviewBlockDTO
#     from blocks.link_to_page import LinkToPageBlockDTO
#     from blocks.numbered_list_item import NumberedListItemBlockDTO
#     from blocks.paragraph import ParagraphBlockDTO
#     from blocks.pdf import PdfBlockDTO
#     from blocks.quote import QuoteBlockDTO
#     from blocks.synced_block import SyncedBlockBlockDTO
#     from blocks.table import TableBlockDTO
#     from blocks.table_of_contents import TableOfContentsBlockDTO
#     from blocks.table_row import TableRowBlockDTO
#     from blocks.template import TemplateBlockDTO
#     from blocks.to_do import ToDoBlockDTO
#     from blocks.toggle import ToggleBlockDTO
#     from blocks.unsupported import UnsupportedBlockDTO
#     from blocks.video import VideoBlockDTO
#     BLOCK_TYPE_MAP: Dict[str, Type[BaseModel]] = {
#         "bookmark": BookmarkBlockDTO,
#         "breadcrumb": BreadcrumbBlockDTO,
#         "bulleted_list_item": BulletedListItemBlockDTO,
#         "callout": CalloutBlockDTO,
#         "child_database": ChildDatabaseBlockDTO,
#         "child_page": ChildPageBlockDTO,
#         "column": ColumnBlockDTO,
#         "column_list": ColumnListBlockDTO,
#         "divider": DividerBlockDTO,
#         "embed": EmbedBlockDTO,
#         "equation": EquationBlockDTO,
#         "file": FileBlockDTO,
#         "heading_1": Heading1BlockDTO,
#         "heading_2": Heading2BlockDTO,
#         "heading_3": Heading3BlockDTO,
#         "image": ImageBlockDTO,
#         "link_preview": LinkPreviewBlockDTO,
#         "link_to_page": LinkToPageBlockDTO,
#         "numbered_list_item": NumberedListItemBlockDTO,
#         "paragraph": ParagraphBlockDTO,
#         "pdf": PdfBlockDTO,
#         "quote": QuoteBlockDTO,
#         "synced_block": SyncedBlockBlockDTO,
#         "table": TableBlockDTO,
#         "table_of_contents": TableOfContentsBlockDTO,
#         "table_row": TableRowBlockDTO,
#         "template": TemplateBlockDTO,
#         "to_do": ToDoBlockDTO,
#         "toggle": ToggleBlockDTO,
#         "unsupported": UnsupportedBlockDTO,
#         "video": VideoBlockDTO,
#     }
#
#     @staticmethod
#     def create_concrete_type_dto(data: json_) -> BaseModel:
#         block_type = data["type"]
#         dto_class = BlockFactory.BLOCK_TYPE_MAP[(block_type)
#         return dto_class(**data)
