from datetime import datetime

from Property import PageProperty, DatabaseProperty


class CreatedTimePage(PageProperty):
    created_time: datetime


class CreatedTimeDatabase(DatabaseProperty):
    pass


class LastEditedTimePage(PageProperty):
    last_edited_time: datetime


class LastEditedTimeDatabase(DatabaseProperty):
    pass
