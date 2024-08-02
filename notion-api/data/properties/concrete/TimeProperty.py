from datetime import datetime

from Property import PageProperty, DatabaseProperty


class CreatedTimePage(PageProperty):
    created_time: datetime


class CreatedTimeDatabase(DatabaseProperty):
    pass


class LastEditedTimePage(PageProperty):
    pass


class LastEditedTimeDatabase(DatabaseProperty):
    pass
