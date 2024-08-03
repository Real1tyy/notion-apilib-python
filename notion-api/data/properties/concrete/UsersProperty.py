from typing import Any

from Property import PageProperty, DatabaseProperty
from UserObject import User


class CreatedByPage(PageProperty):
    created_by: User


class CreatedByDatabase(DatabaseProperty):
    created_by: dict[str, Any]


class LastEditedByPage(PageProperty):
    last_edited_by: User


class LastEditedByDatabase(DatabaseProperty):
    last_edited_by: dict[str, Any]


class PeoplePage(PageProperty):
    people: list[User]


class PeopleDatabase(DatabaseProperty):
    people: dict[str, Any]
