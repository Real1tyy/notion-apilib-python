# Standard Library
from datetime import datetime
from typing import Any

# Third Party
from _properties.property import DatabaseProperty, PageProperty


class CreatedTimePage(PageProperty):
    """
    A model representing a created time property for a page.

    Attributes:
        created_time (datetime): The created time of the page property.
    """
    created_time: datetime


class CreatedTimeDatabase(DatabaseProperty):
    """
    A model representing a created time property for a database.

    Attributes:
        created_time (dict[str, Any]): The dictionary representing the created time property for the database.
    """
    created_time: dict[str, Any]


class LastEditedTimePage(PageProperty):
    """
    A model representing a last edited time property for a page.

    Attributes:
        last_edited_time (datetime): The last edited time of the page property.
    """
    last_edited_time: datetime


class LastEditedTimeDatabase(DatabaseProperty):
    """
    A model representing a last edited time property for a database.

    Attributes:
        last_edited_time (dict[str, Any]): The dictionary representing the last edited time property for the database.
    """
    last_edited_time: dict[str, Any]
