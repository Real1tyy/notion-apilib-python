# Standard Library
from typing import Any

# Third Party
from property import DatabaseProperty, PageProperty
from _data.UserObject import User


class CreatedByPage(PageProperty):
    """
    A model representing a created by property for a page.

    Attributes:
        created_by (User): The user who created the page property.
    """
    created_by: User


class CreatedByDatabase(DatabaseProperty):
    """
    A model representing a created by property for a database.

    Attributes:
        created_by (dict[str, Any]): The dictionary representing the created by property for the database.
    """
    created_by: dict[str, Any]


class LastEditedByPage(PageProperty):
    """
    A model representing a last edited by property for a page.

    Attributes:
        last_edited_by (User): The user who last edited the page property.
    """
    last_edited_by: User


class LastEditedByDatabase(DatabaseProperty):
    """
    A model representing a last edited by property for a database.

    Attributes:
        last_edited_by (dict[str, Any]): The dictionary representing the last edited by property for the database.
    """
    last_edited_by: dict[str, Any]


class PeoplePage(PageProperty):
    """
    A model representing a people property for a page.

    Attributes:
        people (list[User]): The list of users associated with the page property.
    """
    people: list[User]


class PeopleDatabase(DatabaseProperty):
    """
    A model representing a people property for a database.

    Attributes:
        people (dict[str, Any]): The dictionary representing the people property for the database.
    """
    people: dict[str, Any]
