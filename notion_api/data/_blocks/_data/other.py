# Third Party
from _blocks.block import Block, BlockType


class Divider(Block):
    """
    Represents a Divider block.
    """

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.DIVIDER


class ColumnList(Block):
    """
    Represents a Column List block.
    """

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.COLUMN_LIST


class Breadcrumb(Block):
    """
    Represents a Breadcrumb block.
    """

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.BREADCRUMB


class Unsupported(Block):
    """
    Represents an Unsupported block.
    """

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.UNSUPPORTED


__all__ = ["Divider", "ColumnList", "Breadcrumb", "Unsupported"]
