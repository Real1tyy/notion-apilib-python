from datetime import datetime

from _properties.data import CreatedTimePage, CreatedTimeDatabase, LastEditedTimePage, LastEditedTimeDatabase
from _properties.type import PropertyType
from database import Database
from general import _create_page_property, _create_database_property
from page import Page


def create_created_time_page(
        parent: Page, name: str, created_time: datetime) -> CreatedTimePage:
    """
    Factory method to create a CreatedTimePage object.

    Parameters:
        parent (Page): The parent page to which this created time property belongs.
        name (str): The name of the created time property.
        created_time (datetime): The created time of the property.

    Returns:
        CreatedTimePage: A new CreatedTimePage object.
    """
    return _create_page_property(
        CreatedTimePage,
        parent=parent,
        property_type=PropertyType.CREATED_TIME,
        name=name,
        created_time=created_time
    )


def create_created_time_database(
        parent: Database, name: str) -> CreatedTimeDatabase:
    """
    Factory method to create a CreatedTimeDatabase object.

    Parameters:
        parent (Database): The parent database to which this created time property belongs.
        name (str): The name of the created time property.

    Returns:
        CreatedTimeDatabase: A new CreatedTimeDatabase object.
    """
    return _create_database_property(
        CreatedTimeDatabase,
        parent=parent,
        property_type=PropertyType.CREATED_TIME,
        name=name,
        created_time={}
    )


def create_last_edited_time_page(
        parent: Page, name: str, last_edited_time: datetime) -> LastEditedTimePage:
    """
    Factory method to create a LastEditedTimePage object.

    Parameters:
        parent (Page): The parent page to which this last edited time property belongs.
        name (str): The name of the last edited time property.
        last_edited_time (datetime): The last edited time of the property.

    Returns:
        LastEditedTimePage: A new LastEditedTimePage object.
    """
    return _create_page_property(
        LastEditedTimePage,
        parent=parent,
        property_type=PropertyType.LAST_EDITED_TIME,
        name=name,
        last_edited_time=last_edited_time
    )


def create_last_edited_time_database(
        parent: Database, name: str) -> LastEditedTimeDatabase:
    """
    Factory method to create a LastEditedTimeDatabase object.

    Parameters:
        parent (Database): The parent database to which this last edited time property belongs.
        name (str): The name of the last edited time property.

    Returns:
        LastEditedTimeDatabase: A new LastEditedTimeDatabase object.
    """
    return _create_database_property(
        LastEditedTimeDatabase,
        parent=parent,
        property_type=PropertyType.LAST_EDITED_TIME,
        name=name,
        ast_edited_time={}
    )
