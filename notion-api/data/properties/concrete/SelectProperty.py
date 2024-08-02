from uuid import UUID

from pydantic import BaseModel, Field

from Property import PageProperty, DatabaseProperty


class CheckboxPage(PageProperty):
    checkbox: bool


class CheckboxDatabase(DatabaseProperty):
    pass


class Option(BaseModel):
    id: str = Field(exclude=True)
    name: str
    color: str = Field(exclude=True)


class OptionStructure(BaseModel):
    options: list[Option]


class MultiSelectPage(PageProperty):
    multi_select: OptionStructure


class MultiSelectDatabase(DatabaseProperty):
    multi_select: OptionStructure


class SelectPage(PageProperty):
    select: Option


class SelectDatabase(DatabaseProperty):
    select: OptionStructure


class StatusPage(PageProperty):
    status: Option


class Group(Option):
    option_ids: list[UUID]


class StatusDatabaseStructure(BaseModel):
    options: list[Option]
    groups: list[Group]


class StatusDatabase(DatabaseProperty):
    status: StatusDatabaseStructure
