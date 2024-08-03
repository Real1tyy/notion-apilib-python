from datetime import datetime
from typing import Any

from Property import PageProperty, DatabaseProperty


class CreatedTimePage(PageProperty):
    created_time: datetime


class CreatedTimeDatabase(DatabaseProperty):
    created_time: dict[str, Any]


class LastEditedTimePage(PageProperty):
    last_edited_time: datetime


class LastEditedTimeDatabase(DatabaseProperty):
    last_edited_time: dict[str, Any]
