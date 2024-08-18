# Standard Library

# First Party
from notion_apilib.data.structures import FileAttributes, ResourcesAttributes

from ..block import Block, BlockType


class File(Block):
    """
    Represents a File block.

    :param file: Attributes for the file block.
    :type file: FileAttributes
    """

    file: FileAttributes

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.FILE


class Image(Block):
    """
    Represents an Image block.

    :param image: Attributes for the image block.
    :type image: ResourcesAttributes
    """

    image: ResourcesAttributes

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.IMAGE


class Pdf(Block):
    """
    Represents a PDF block.

    :param pdf: Attributes for the PDF block.
    :type pdf: ResourcesAttributes
    """

    pdf: ResourcesAttributes

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.PDF


class Video(Block):
    """
    Represents a Video block.

    :param video: Attributes for the video block.
    :type video: ResourcesAttributes
    """

    video: ResourcesAttributes

    @classmethod
    def get_associated_block_type(cls) -> BlockType:
        return BlockType.VIDEO


__all__ = ["File", "Image", "Pdf", "Video"]
