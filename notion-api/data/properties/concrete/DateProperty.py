from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from Property import PageProperty, DatabaseProperty


class DateStructure(BaseModel):
    end: Optional[datetime]
    start: datetime
    time_zone: Optional[str]


class DatePage(PageProperty):
    date: DateStructure


class DateDatabase(DatabaseProperty):
    pass
