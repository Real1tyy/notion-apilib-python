# Standard Library
from typing import Literal, Optional

# Third Party
from FileObject import External, FileObject
from pydantic import BaseModel
from _data.RichText import RichText

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
