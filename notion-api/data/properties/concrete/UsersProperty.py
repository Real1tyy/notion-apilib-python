from Property import PageProperty, DatabaseProperty
from UserObject import User


class CreatedByPage(PageProperty):
    created_by: User


class CreatedByDatabase(DatabaseProperty):
    pass


class LastEditedByPage(PageProperty):
    last_edited_by: User


class LastEditedByDatabase(DatabaseProperty):
    pass


class PeoplePage(PageProperty):
    people: list[User]


class PeopleDatabase(DatabaseProperty):
    pass
