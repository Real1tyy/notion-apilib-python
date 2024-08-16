# Standard Library
from typing import Optional, Type, TypeVar

# First Party
from ._general import _create_block
from ..data import File, Image, Pdf, Video
from notion_api.data.structures import (
    External,
    FileObject,
    Parent,
    ResourcesAttributes,
    file_type,
)

T = TypeVar("T", File, Image, Pdf, Video)


def _determine_file_type(
    external: Optional[External], file: Optional[FileObject]
) -> file_type:
    """
    Determine the type of file based on the provided parameters.

    Parameters
    ----------
    external : Optional[External]
        The external file object, if any.
    file : Optional[FileObject]
        The file object, if any.

    Returns
    -------
    file_type
        The type of the file, either 'external' or 'file'.

    Raises
    ------
    ValueError
        If neither external nor file is provided.
    """
    if external is None and file is None:
        raise ValueError("Either external or file should be provided")
    if external is not None:
        return "external"
    else:
        return "file"


def _create_resources_object(
    resource: Type[T],
    parent: Parent,
    external: Optional[External] = None,
    file: Optional[FileObject] = None,
) -> T:
    """
    Factory method to create Resources object
    :param resource: the class of the resource to create
    :param parent: parent object
    :param external: external details (optional)
    :param file: internal file details (optional)
    :return: newly created Resources Object
    """
    _type = _determine_file_type(external, file)

    return _create_block(
        resource,
        parent=parent,
        block_type_specific_params=ResourcesAttributes(
            type=_type, external=external, file=file
        ),
    )


def create_file(
    parent: Parent,
    external: Optional[External] = None,
    file: Optional[FileObject] = None,
) -> File:
    """
    Factory method to create a File object.

    :param parent: The parent object to which this file belongs.
    :param external: Optional external details for the file.
    :param file: Optional internal file details.
    :return: A newly created File object.
    """
    return _create_resources_object(File, parent, external, file)


def create_image(
    parent: Parent,
    external: Optional[External] = None,
    file: Optional[FileObject] = None,
) -> Image:
    """
    Factory method to create an Image object.

    :param parent: The parent object to which this image belongs.
    :param external: Optional external details for the image.
    :param file: Optional internal file details.
    :return: A newly created Image object.
    """
    return _create_resources_object(Image, parent, external, file)


def create_pdf(
    parent: Parent,
    external: Optional[External] = None,
    file: Optional[FileObject] = None,
) -> Pdf:
    """
    Factory method to create a Pdf object.

    :param parent: The parent object to which this PDF belongs.
    :param external: Optional external details for the PDF.
    :param file: Optional internal file details.
    :return: A newly created Pdf object.
    """
    return _create_resources_object(Pdf, parent, external, file)


def create_video(
    parent: Parent,
    external: Optional[External] = None,
    file: Optional[FileObject] = None,
) -> Video:
    """
    Factory method to create a Video object.

    :param parent: The parent object to which this video belongs.
    :param external: Optional external details for the video.
    :param file: Optional internal file details.
    :return: A newly created Video object.
    """
    return _create_resources_object(Video, parent, external, file)


__all__ = ["create_file", "create_image", "create_pdf", "create_video"]
