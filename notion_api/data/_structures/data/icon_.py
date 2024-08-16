# Standard Library
from typing import Optional

# Third Party
from pydantic import BaseModel

# First Party
from ..types_ import file_type
from .file_ import FileObject, External


class Emoji(BaseModel):
    """
    Represents an Emoji in the Notion API.

    Attributes
    ----------
    emoji : str
        The emoji character.
    type : str
        The type of the emoji.
    """

    emoji: str
    type: str


class Icon(BaseModel, arbitrary_types_allowed=True):
    """
    Represents an Icon in the Notion API.

    Attributes
    ----------
    type : file_type
        The type of the icon, either 'external' or 'file'.
    external : Optional[External]
        The external file object, if any.
    file : Optional[FileObject]
        The file object, if any.
    """

    type: file_type
    external: Optional[External] = None
    file: Optional[FileObject] = None


__all__ = ["Emoji", "Icon"]
