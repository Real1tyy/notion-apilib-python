from typing import Optional, Literal

from pydantic import BaseModel

from Block import Block, _create_block_object
from BlockType import BlockType
from FileObject import External, FileObject
from Parent import Parent
from RichText import RichText

file_type = Literal['external', 'file']


def determine_file_type(external: Optional[External], file: Optional[FileObject]) -> file_type:
    if external is None and file is None:
        raise ValueError("Either external or file should be provided")
    if external is not None:
        return "external"
    else:
        return "file"


class ResourcesAttributes(BaseModel):
    type: file_type
    external: Optional[External] = None
    file: Optional[FileObject] = None


class FileAttributes(ResourcesAttributes):
    caption: list[RichText]
    name: str


class File(Block):
    file: FileAttributes


def create_file_object(
        parent: Parent, caption: list[RichText], name: str, external: Optional[External] = None,
        file: Optional[FileObject] = None) -> File:
    """
    Factory method to create File object
    :param parent: parent object
    :param caption: caption for the file
    :param name: name of the file
    :param external: external file details (optional)
    :param file: internal file details (optional)
    :return: newly created File Object
    """
    _type = determine_file_type(external, file)

    return _create_block_object(
        File,
        parent=parent,
        block_type=BlockType.FILE,
        file=FileAttributes(
            type=_type,
            external=external,
            file=file,
            caption=caption,
            name=name
        )
    )


class Image(Block):
    image: ResourcesAttributes


def create_image_object(
        parent: Parent, external: Optional[External] = None, file: Optional[FileObject] = None) -> Image:
    """
    Factory method to create Image object
    :param parent: parent object
    :param external: external image details (optional)
    :param file: internal image details (optional)
    :return: newly created Image Object
    """
    _type = determine_file_type(external, file)

    return _create_block_object(
        Image,
        parent=parent,
        block_type=BlockType.IMAGE,
        image=ResourcesAttributes(
            type=_type,
            external=external,
            file=file
        )
    )


class Pdf(Block):
    pdf: ResourcesAttributes


def create_pdf_object(parent: Parent, external: Optional[External] = None, file: Optional[FileObject] = None) -> Pdf:
    """
    Factory method to create Pdf object
    :param parent: parent object
    :param external: external pdf details (optional)
    :param file: internal pdf details (optional)
    :return: newly created Pdf Object
    """
    _type = determine_file_type(external, file)
    return _create_block_object(
        Pdf,
        parent=parent,
        block_type=BlockType.PDF,
        pdf=ResourcesAttributes(
            type=_type,
            external=external,
            file=file
        )
    )


class Video(Block):
    video: ResourcesAttributes


def create_video_object(
        parent: Parent, external: Optional[External] = None, file: Optional[FileObject] = None) -> Video:
    """
    Factory method to create Video object
    :param parent: parent object
    :param external: external video details (optional)
    :param file: internal video details (optional)
    :return: newly created Video Object
    """
    _type = determine_file_type(external, file)
    return _create_block_object(
        Video,
        parent=parent,
        block_type=BlockType.VIDEO,
        video=ResourcesAttributes(
            type=_type,
            external=external,
            file=file
        )
    )
