from typing import Optional

from pydantic import BaseModel

from Block import Block
from FileObject import External, FileObject
from RichText import RichText


class ResourcesAttributes(BaseModel):
    type: str
    external: Optional[External] = None
    file: Optional[FileObject] = None


class FileAttributes(ResourcesAttributes):
    caption: list[RichText]
    name: str


class File(Block):
    file: FileAttributes


class Image(Block):
    image: ResourcesAttributes


class Pdf(Block):
    pdf: ResourcesAttributes


class Video(Block):
    video: ResourcesAttributes
