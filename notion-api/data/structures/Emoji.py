from typing import Literal, Optional

from pydantic import BaseModel

from FileObject import External, FileObject

file_type = Literal['external', 'file']


class Emoji(BaseModel):
    emoji: str
    type: str


class Icon(BaseModel):
    type: file_type
    external: Optional[External] = None
    file: Optional[FileObject] = None
