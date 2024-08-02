from datetime import datetime
from typing import Optional

from Property import PageProperty, DatabaseProperty


class DatePage(PageProperty):
    end: Optional[datetime]
    start: datetime
    time_zone: Optional[str]


class DateDatabase(DatabaseProperty):
    pass
