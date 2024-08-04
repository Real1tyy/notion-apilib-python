from UserObject import User
from _properties.type import PropertyType
from database import Database
from general import _create_page_property, _create_database_property
from page import Page
from users import PeoplePage, LastEditedByPage, CreatedByPage, CreatedByDatabase, LastEditedByDatabase, \
    PeopleDatabase


def create_created_by_page(
        parent: Page, name: str, created_by: User) -> CreatedByPage:
    """
    Factory method to create a CreatedByPage object.

    Parameters:
        parent (Page): The parent page to which this created by property belongs.
        name (str): The name of the created by property.
        created_by (User): The user who created the property.

    Returns:
        CreatedByPage: A new CreatedByPage object.
    """
    return _create_page_property(
        CreatedByPage,
        parent=parent,
        property_type=PropertyType.CREATED_BY,
        name=name,
        created_by=created_by
    )


def create_created_by_database(
        parent: Database, name: str) -> CreatedByDatabase:
    """
    Factory method to create a CreatedByDatabase object.

    Parameters:
        parent (Database): The parent database to which this created by property belongs.
        name (str): The name of the created by property.

    Returns:
        CreatedByDatabase: A new CreatedByDatabase object.
    """
    return _create_database_property(
        CreatedByDatabase,
        parent=parent,
        property_type=PropertyType.CREATED_BY,
        name=name,
        created_by={}
    )


def create_last_edited_by_page(
        parent: Page, name: str, last_edited_by: User) -> LastEditedByPage:
    """
    Factory method to create a LastEditedByPage object.

    Parameters:
        parent (Page): The parent page to which this last edited by property belongs.
        name (str): The name of the last edited by property.
        last_edited_by (User): The user who last edited the property.

    Returns:
        LastEditedByPage: A new LastEditedByPage object.
    """
    return _create_page_property(
        LastEditedByPage,
        parent=parent,
        property_type=PropertyType.LAST_EDITED_BY,
        name=name,
        last_edited_by=last_edited_by
    )


def create_last_edited_by_database(
        parent: Database, name: str) -> LastEditedByDatabase:
    """
    Factory method to create a LastEditedByDatabase object.

    Parameters:
        parent (Database): The parent database to which this last edited by property belongs.
        name (str): The name of the last edited by property.

    Returns:
        LastEditedByDatabase: A new LastEditedByDatabase object.
    """
    return _create_database_property(
        LastEditedByDatabase,
        parent=parent,
        property_type=PropertyType.LAST_EDITED_BY,
        name=name,
        last_edited_by={}
    )


def create_people_page(
        parent: Page, name: str, people: list[User]) -> PeoplePage:
    """
    Factory method to create a PeoplePage object.

    Parameters:
        parent (Page): The parent page to which this people property belongs.
        name (str): The name of the people property.
        people (list[User]): The list of users associated with the property.

    Returns:
        PeoplePage: A new PeoplePage object.
    """
    return _create_page_property(
        PeoplePage,
        parent=parent,
        property_type=PropertyType.PEOPLE,
        name=name,
        people=people
    )


def create_people_database(
        parent: Database, name: str) -> PeopleDatabase:
    """
    Factory method to create a PeopleDatabase object.

    Parameters:
        parent (Database): The parent database to which this people property belongs.
        name (str): The name of the people property.

    Returns:
        PeopleDatabase: A new PeopleDatabase object.
    """
    return _create_database_property(
        PeopleDatabase,
        parent=parent,
        property_type=PropertyType.PEOPLE,
        name=name,
        people={}
    )
