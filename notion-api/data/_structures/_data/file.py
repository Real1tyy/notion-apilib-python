# Standard Library
from datetime import datetime
from typing import Optional

# Third Party
from pydantic import BaseModel

from _structures.data import RichText
from types_ import file_type


class FileObject(BaseModel):
    """
    Represents a file object in the Notion API.

    Attributes
    ----------
    url : str
        The URL of the file.
    expiry_time : datetime
        The expiry time of the file URL.
    """
    url: str
    expiry_time: datetime


class External(BaseModel):
    """
    Represents an external file in the Notion API.

    Attributes
    ----------
    url : str
        The URL of the external file.
    """
    url: str


def determine_file_type(external: Optional[External], file: Optional[FileObject]) -> file_type:
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


class ResourcesAttributes(BaseModel):
    """
    Represents the attributes of a resource in the Notion API.

    Attributes
    ----------
    type : file_type
        The type of the resource, either 'external' or 'file'.
    external : Optional[External]
        The external file object, if any.
    file : Optional[FileObject]
        The file object, if any.
    """
    type: file_type
    external: Optional[External] = None
    file: Optional[FileObject] = None


class FileAttributes(ResourcesAttributes):
    """
    Represents the attributes of a file in the Notion API.

    Attributes
    ----------
    caption : list[RichText]
        The caption of the file.
    name : str
        The name of the file.
    """
    caption: list[RichText]
    name: str
