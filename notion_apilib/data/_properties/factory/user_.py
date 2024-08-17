# First Party
from notion_apilib.data.structures import User

from ..data import CreatedByDatabase, CreatedByPage, LastEditedByDatabase, LastEditedByPage, PeopleDatabase, PeoplePage
from ._general import _create_database_property, _create_page_property


def create_created_by_page(
        parent: "Page", name: str, created_by: User
) -> CreatedByPage:
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
        CreatedByPage, parent=parent, name=name, property_specific_params=created_by
    )


def create_created_by_database(parent: "Database", name: str) -> CreatedByDatabase:
    """
    Factory method to create a CreatedByDatabase object.

    Parameters:
        parent (Database): The parent database to which this created by property belongs.
        name (str): The name of the created by property.

    Returns:
        CreatedByDatabase: A new CreatedByDatabase object.
    """
    return _create_database_property(
        CreatedByDatabase, parent=parent, name=name, property_specific_params={}
    )


def create_last_edited_by_page(
        parent: "Page", name: str, last_edited_by: User
) -> LastEditedByPage:
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
        name=name,
        property_specific_params=last_edited_by,
    )


def create_last_edited_by_database(
        parent: "Database", name: str
) -> LastEditedByDatabase:
    """
    Factory method to create a LastEditedByDatabase object.

    Parameters:
        parent (Database): The parent database to which this last edited by property belongs.
        name (str): The name of the last edited by property.

    Returns:
        LastEditedByDatabase: A new LastEditedByDatabase object.
    """
    return _create_database_property(
        LastEditedByDatabase, parent=parent, name=name, property_specific_params={}
    )


def create_people_page(parent: "Page", name: str, people: list[User]) -> PeoplePage:
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
        PeoplePage, parent=parent, name=name, property_specific_params=people
    )


def create_people_database(parent: "Database", name: str) -> PeopleDatabase:
    """
    Factory method to create a PeopleDatabase object.

    Parameters:
        parent (Database): The parent database to which this people property belongs.
        name (str): The name of the people property.

    Returns:
        PeopleDatabase: A new PeopleDatabase object.
    """
    return _create_database_property(
        PeopleDatabase, parent=parent, name=name, property_specific_params={}
    )


__all__ = [
    "create_created_by_page",
    "create_created_by_database",
    "create_last_edited_by_page",
    "create_last_edited_by_database",
    "create_people_page",
    "create_people_database",
]
