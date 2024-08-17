# file_factory.py

# Standard Library
from datetime import datetime
from typing import List, Optional

from ..data import External, FileAttributes, FileObject, ResourcesAttributes, RichText
from ..types_ import file_type


def create_file_object(url: str, expiry_time: datetime) -> FileObject:
    """
    Factory method to create a FileObject.

    Parameters
    ----------
    url : str
        The URL of the file.
    expiry_time : datetime
        The expiry time of the file URL.

    Returns
    -------
    FileObject
        A new FileObject instance.
    """
    return FileObject(url=url, expiry_time=expiry_time)


def create_external(url: str) -> External:
    """
    Factory method to create an External file object.

    Parameters
    ----------
    url : str
        The URL of the external file.

    Returns
    -------
    External
        A new External instance.
    """
    return External(url=url)


def create_resources_attributes(
    type_: file_type,
    external: Optional[External] = None,
    file: Optional[FileObject] = None,
) -> ResourcesAttributes:
    """
    Factory method to create ResourcesAttributes.

    Parameters
    ----------
    type_ : str
        The type of the resource, either 'external' or 'file'.
    external : Optional[External]
        The external file object, if any. Defaults to None.
    file : Optional[FileObject]
        The file object, if any. Defaults to None.

    Returns
    -------
    ResourcesAttributes
        A new ResourcesAttributes instance.

    Raises
    ------
    ValueError
        If neither external nor file is provided.
    """
    if external is None and file is None:
        raise ValueError("Either external or file should be provided")

    return ResourcesAttributes(type=type_, external=external, file=file)


def create_file_attributes(
    type_: file_type,
    caption: List[RichText],
    name: str,
    external: Optional[External] = None,
    file: Optional[FileObject] = None,
) -> FileAttributes:
    """
    Factory method to create FileAttributes.

    Parameters
    ----------
    type_ : str
        The type of the resource, either 'external' or 'file'.
    caption : List[RichText]
        The caption of the file.
    name : str
        The name of the file.
    external : Optional[External]
        The external file object, if any. Defaults to None.
    file : Optional[FileObject]
        The file object, if any. Defaults to None.

    Returns
    -------
    FileAttributes
        A new FileAttributes instance.

    Raises
    ------
    ValueError
        If neither external nor file is provided.
    """
    if external is None and file is None:
        raise ValueError("Either external or file should be provided")

    return FileAttributes(
        type=type_, caption=caption, name=name, external=external, file=file
    )


__all__ = [
    "create_file_object",
    "create_external",
    "create_resources_attributes",
    "create_file_attributes",
]
