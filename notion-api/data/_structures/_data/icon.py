# Standard Library
from typing import Literal, Optional

# Third Party
from FileObject import External, FileObject
from pydantic import BaseModel

file_type = Literal['external', 'file']


class Emoji(BaseModel):
    emoji: str
    type: str


class Icon(BaseModel):
    type: file_type
    external: Optional[External] = None
    file: Optional[FileObject] = None
