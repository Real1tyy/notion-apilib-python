# Standard Library

from ResourcesAttributes import FileAttributes, ResourcesAttributes
# Third Party
from blocks.block import Block


class File(Block):
    """
    Represents a File block.

    :param file: Attributes for the file block.
    :type file: FileAttributes
    """
    file: FileAttributes


class Image(Block):
    """
    Represents an Image block.

    :param image: Attributes for the image block.
    :type image: ResourcesAttributes
    """
    image: ResourcesAttributes


class Pdf(Block):
    """
    Represents a PDF block.

    :param pdf: Attributes for the PDF block.
    :type pdf: ResourcesAttributes
    """
    pdf: ResourcesAttributes


class Video(Block):
    """
    Represents a Video block.

    :param video: Attributes for the video block.
    :type video: ResourcesAttributes
    """
    video: ResourcesAttributes
