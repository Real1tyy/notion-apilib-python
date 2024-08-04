from datetime import datetime
from typing import Optional

from _properties.type_ import PropertyType
from database import Database
from date import DatePage, DateStructure, DateDatabase
from general import _create_page_property, _create_database_property
from page import Page


def create_date_page(
        parent: Page, name: str, start: datetime, end: Optional[datetime] = None, time_zone: Optional[
            str] = None) -> DatePage:
    """
    Factory method to create a DatePage object.

    Parameters:
        parent (Page): The parent page to which this date property belongs.
        name (str): The name of the date property.
        start (datetime): The start datetime of the date property.
        end (Optional[datetime]): The optional end datetime of the date property.
        time_zone (Optional[str]): The optional time zone of the date property.

    Returns:
        DatePage: A new DatePage object.
    """
    return _create_page_property(
        DatePage,
        parent=parent,
        property_type=PropertyType.DATE,
        name=name,
        date=DateStructure(end=end, start=start, time_zone=time_zone)
    )


def create_date_database(
        parent: Database, name: str) -> DateDatabase:
    """
    Factory method to create a DateDatabase object.

    Parameters:
        parent (Database): The parent database to which this date property belongs.
        name (str): The name of the date property.

    Returns:
        DateDatabase: A new DateDatabase object.
    """
    return _create_database_property(
        DateDatabase,
        parent=parent,
        property_type=PropertyType.DATE,
        name=name,
        date={}
    )
