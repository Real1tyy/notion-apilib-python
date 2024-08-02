from typing import Optional

from pydantic import BaseModel

from Property import PageProperty, DatabaseProperty


class NumberPage(PageProperty):
    number: float


class NumberStructure(BaseModel):
    format: str


class NumberDatabase(DatabaseProperty):
    number: NumberStructure


class UniqueIdStructure(BaseModel):
    number: float
    prefix: Optional[str] = None


class UniqueIdPage(PageProperty):
    unique_id: UniqueIdStructure


class UniqueIdDatabase(DatabaseProperty):
    pass
