# Standard Library
from datetime import datetime
from typing import Any, Optional

# Third Party
from pydantic import BaseModel

# First Party
from ..property import DatabaseProperty, PageProperty
from ..type_ import PropertyType


class DateStructure(BaseModel):
    """
    A model representing a date structure with a start datetime, optional end datetime, and optional time zone.

    Attributes:
        start (datetime): The start datetime of the date structure.
        end (Optional[datetime]): The optional end datetime of the date structure.
        time_zone (Optional[str]): The optional time zone of the date structure.
    """

    end: Optional[datetime]
    start: datetime
    time_zone: Optional[str]


class DatePage(PageProperty):
    """
    A model representing a date property for a page.

    Attributes:
        date (Optional[DateStructure]): The optional date structure of the page property.
    """

    date: Optional[DateStructure]

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.DATE


class DateDatabase(DatabaseProperty):
    """
    A model representing a date property for a database.

    Attributes:
        date (dict[str, Any]): The dictionary representing the date property for the database.
    """

    date: dict[str, Any]

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.DATE


__all__ = ["DatePage", "DateDatabase"]
