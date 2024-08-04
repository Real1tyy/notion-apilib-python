from datetime import datetime
from typing import Optional

from DateProperty import DatePage, DateStructure
from Page import Page
from PropertyType import PropertyType
from factory.general import _create_page_property


def create_date_page(
        parent: Page, name: str, start: datetime, end: Optional[datetime] = None, time_zone: Optional[
            str] = None, id_: Optional[str] = None) -> DatePage:
    """
    Factory method to create a DatePage object.

    Parameters:
        parent (Page): The parent page to which this date property belongs.
        name (str): The name of the date property.
        start (datetime): The start datetime of the date property.
        end (Optional[datetime]): The optional end datetime of the date property.
        time_zone (Optional[str]): The optional time zone of the date property.
        id_ (Optional[str]): The optional ID of the date property.

    Returns:
        DatePage: A new DatePage object.
    """
    return _create_page_property(
        DatePage,
        parent=parent,
        property_type=PropertyType.DATE,
        name=name,
        id_=id_,
        date=DateStructure(end=end, start=start, time_zone=time_zone)
    )
