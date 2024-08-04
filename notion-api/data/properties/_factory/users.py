from typing import Optional

from Page import Page
from PropertyType import PropertyType
from UserObject import User
from UsersProperty import PeoplePage, LastEditedByPage, CreatedByPage
from factory.general import _create_page_property


def create_created_by_page(
        parent: Page, name: str, created_by: User, id_: Optional[str] = None) -> CreatedByPage:
    """
    Factory method to create a CreatedByPage object.

    Parameters:
        parent (Page): The parent page to which this created by property belongs.
        name (str): The name of the created by property.
        created_by (User): The user who created the property.
        id_ (Optional[str]): The optional ID of the created by property.

    Returns:
        CreatedByPage: A new CreatedByPage object.
    """
    return _create_page_property(
        CreatedByPage,
        parent=parent,
        property_type=PropertyType.CREATED_BY,
        name=name,
        id_=id_,
        created_by=created_by
    )


def create_last_edited_by_page(
        parent: Page, name: str, last_edited_by: User, id_: Optional[str] = None) -> LastEditedByPage:
    """
    Factory method to create a LastEditedByPage object.

    Parameters:
        parent (Page): The parent page to which this last edited by property belongs.
        name (str): The name of the last edited by property.
        last_edited_by (User): The user who last edited the property.
        id_ (Optional[str]): The optional ID of the last edited by property.

    Returns:
        LastEditedByPage: A new LastEditedByPage object.
    """
    return _create_page_property(
        LastEditedByPage,
        parent=parent,
        property_type=PropertyType.LAST_EDITED_BY,
        name=name,
        id_=id_,
        last_edited_by=last_edited_by
    )


def create_people_page(
        parent: Page, name: str, people: list[User], id_: Optional[str] = None) -> PeoplePage:
    """
    Factory method to create a PeoplePage object.

    Parameters:
        parent (Page): The parent page to which this people property belongs.
        name (str): The name of the people property.
        people (list[User]): The list of users associated with the property.
        id_ (Optional[str]): The optional ID of the people property.

    Returns:
        PeoplePage: A new PeoplePage object.
    """
    return _create_page_property(
        PeoplePage,
        parent=parent,
        property_type=PropertyType.PEOPLE,
        name=name,
        id_=id_,
        people=people
    )
