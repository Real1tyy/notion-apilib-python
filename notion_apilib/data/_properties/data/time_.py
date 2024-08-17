# Standard Library
from datetime import datetime
from typing import Any

from ..property import DatabaseProperty, PageProperty
from ..type_ import PropertyType


class CreatedTimePage(PageProperty):
    """
    A model representing a created time property for a page.

    Attributes:
        created_time (datetime): The created time of the page property.
    """

    created_time: datetime

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.CREATED_TIME


class CreatedTimeDatabase(DatabaseProperty):
    """
    A model representing a created time property for a database.

    Attributes:
        created_time (dict[str, Any]): The dictionary representing the created time property for the database.
    """

    created_time: dict[str, Any]

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.CREATED_TIME


class LastEditedTimePage(PageProperty):
    """
    A model representing a last edited time property for a page.

    Attributes:
        last_edited_time (datetime): The last edited time of the page property.
    """

    last_edited_time: datetime

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.LAST_EDITED_TIME


class LastEditedTimeDatabase(DatabaseProperty):
    """
    A model representing a last edited time property for a database.

    Attributes:
        last_edited_time (dict[str, Any]): The dictionary representing the last edited time property for the database.
    """

    last_edited_time: dict[str, Any]

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.LAST_EDITED_TIME


__all__ = [
    "CreatedTimePage",
    "CreatedTimeDatabase",
    "LastEditedTimePage",
    "LastEditedTimeDatabase",
]
