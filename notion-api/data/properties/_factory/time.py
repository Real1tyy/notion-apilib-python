from datetime import datetime
from typing import Optional

from Page import Page
from PropertyType import PropertyType
from TimeProperty import LastEditedTimePage, CreatedTimePage
from _factory.general import _create_page_property


def create_created_time_page(
        parent: Page, name: str, created_time: datetime, id_: Optional[str] = None) -> CreatedTimePage:
    """
    Factory method to create a CreatedTimePage object.

    Parameters:
        parent (Page): The parent page to which this created time property belongs.
        name (str): The name of the created time property.
        created_time (datetime): The created time of the property.
        id_ (Optional[str]): The optional ID of the created time property.

    Returns:
        CreatedTimePage: A new CreatedTimePage object.
    """
    return _create_page_property(
        CreatedTimePage,
        parent=parent,
        property_type=PropertyType.CREATED_TIME,
        name=name,
        id_=id_,
        created_time=created_time
    )


def create_last_edited_time_page(
        parent: Page, name: str, last_edited_time: datetime, id_: Optional[str] = None) -> LastEditedTimePage:
    """
    Factory method to create a LastEditedTimePage object.

    Parameters:
        parent (Page): The parent page to which this last edited time property belongs.
        name (str): The name of the last edited time property.
        last_edited_time (datetime): The last edited time of the property.
        id_ (Optional[str]): The optional ID of the last edited time property.

    Returns:
        LastEditedTimePage: A new LastEditedTimePage object.
    """
    return _create_page_property(
        LastEditedTimePage,
        parent=parent,
        property_type=PropertyType.LAST_EDITED_TIME,
        name=name,
        id_=id_,
        last_edited_time=last_edited_time
    )
