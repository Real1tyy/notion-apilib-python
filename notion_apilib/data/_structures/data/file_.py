# Standard Library
from datetime import datetime
from typing import Optional, Any

# Third Party
from pydantic import BaseModel, model_validator

# First Party
import notion_apilib.data._structures.data.text_ as text

from ..types_ import file_type
from ..._util import check_if_exactly_one_not_none_val


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


class ResourcesAttributes(BaseModel, arbitrary_types_allowed=True):
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

    @classmethod
    @model_validator(mode="after")
    def parse_properties(cls, v: Any):
        properties = [v.external, v.file]
        if check_if_exactly_one_not_none_val(properties):
            raise ValueError(
                f"Only one of the values from: {properties} can be provided."
            )
        return v


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

    caption: list[text.RichText]
    name: str


__all__ = ["External", "FileAttributes", "FileObject", "ResourcesAttributes"]
