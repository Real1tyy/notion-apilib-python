from typing import TypeVar, Type, Optional

from FileObject import External, FileObject
from Parent import Parent
from ResourcesAttributes import determine_file_type, ResourcesAttributes
from _data.resources import File, Image, Pdf, Video
from block import _create_block
from type import BlockType

T = TypeVar('T', bound='Block')


def _create_resources_object(
        resource: Type[T], parent: Parent, external: Optional[External] = None, file: Optional[FileObject] = None) -> T:
    """
    Factory method to create Resources object
    :param resource: the class of the resource to create
    :param parent: parent object
    :param external: external details (optional)
    :param file: internal file details (optional)
    :return: newly created Resources Object
    """
    _type = determine_file_type(external, file)

    return _create_block(
        resource,
        parent=parent,
        block_type=BlockType.IMAGE,
        image=ResourcesAttributes(
            type=_type,
            external=external,
            file=file
        )
    )


def create_file(parent: Parent, external: Optional[External] = None, file: Optional[FileObject] = None) -> File:
    """
    Factory method to create a File object.

    :param parent: The parent object to which this file belongs.
    :param external: Optional external details for the file.
    :param file: Optional internal file details.
    :return: A newly created File object.
    """
    return _create_resources_object(File, parent, external, file)


def create_image(
        parent: Parent, external: Optional[External] = None, file: Optional[FileObject] = None) -> Image:
    """
    Factory method to create an Image object.

    :param parent: The parent object to which this image belongs.
    :param external: Optional external details for the image.
    :param file: Optional internal file details.
    :return: A newly created Image object.
    """
    return _create_resources_object(Image, parent, external, file)


def create_pdf(parent: Parent, external: Optional[External] = None, file: Optional[FileObject] = None) -> Pdf:
    """
    Factory method to create a Pdf object.

    :param parent: The parent object to which this PDF belongs.
    :param external: Optional external details for the PDF.
    :param file: Optional internal file details.
    :return: A newly created Pdf object.
    """
    return _create_resources_object(Pdf, parent, external, file)


def create_video(
        parent: Parent, external: Optional[External] = None, file: Optional[FileObject] = None) -> Video:
    """
    Factory method to create a Video object.

    :param parent: The parent object to which this video belongs.
    :param external: Optional external details for the video.
    :param file: Optional internal file details.
    :return: A newly created Video object.
    """
    return _create_resources_object(Video, parent, external, file)
