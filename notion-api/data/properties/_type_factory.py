# Third Party
from PropertyType import PropertyType
from custom_types import json_
from date import DateDatabase, DatePage
from formula import FormulaDatabase, FormulaPage
from number import NumberDatabase, NumberPage, UniqueIdDatabase, UniqueIdPage
from option import (
    CheckboxDatabase,
    CheckboxPage,
    MultiSelectDatabase,
    MultiSelectPage,
    SelectDatabase,
    SelectPage,
    StatusDatabase,
    StatusPage,
)
from relation import RelationDatabase, RelationPage, RollupDatabase, RollupPage
from resources import (
    EmailDatabase,
    EmailPage,
    FilesDatabase,
    FilesPage,
    PhoneNumberDatabase,
    PhoneNumberPage,
    UrlDatabase,
    UrlPage,
)
from text import RichTextDatabase, RichTextPage, TitleDatabase, TitlePage
from time import CreatedTimeDatabase, CreatedTimePage, LastEditedTimeDatabase, LastEditedTimePage
from users import (
    CreatedByDatabase,
    CreatedByPage,
    LastEditedByDatabase,
    LastEditedByPage,
    PeopleDatabase,
    PeoplePage,
)

PROPERTY_TYPE_MAP = {
    "checkbox": (CheckboxPage, CheckboxDatabase),
    "created_by": (CreatedByPage, CreatedByDatabase),
    "created_time": (CreatedTimePage, CreatedTimeDatabase),
    "date": (DatePage, DateDatabase),
    "email": (EmailPage, EmailDatabase),
    "files": (FilesPage, FilesDatabase),
    "formula": (FormulaPage, FormulaDatabase),
    "last_edited_by": (LastEditedByPage, LastEditedByDatabase),
    "last_edited_time": (LastEditedTimePage, LastEditedTimeDatabase),
    "multi_select": (MultiSelectPage, MultiSelectDatabase),
    "number": (NumberPage, NumberDatabase),
    "people": (PeoplePage, PeopleDatabase),
    "phone_number": (PhoneNumberPage, PhoneNumberDatabase),
    "relation": (RelationPage, RelationDatabase),
    "rollup": (RollupPage, RollupDatabase),
    "status": (StatusPage, StatusDatabase),
    "unique_id": (UniqueIdPage, UniqueIdDatabase),
    "url": (UrlPage, UrlDatabase),
    "select": (SelectPage, SelectDatabase),
    "title": (TitlePage, TitleDatabase),
    "rich_text": (RichTextPage, RichTextDatabase)
}


def create_concrete_page_property_type(data: json_):
    property_type = PropertyType(data["type"])
    return PROPERTY_TYPE_MAP[property_type][0](**data)


def create_concrete_database_property_type(data: json_):
    property_type = PropertyType(data["type"])
    return PROPERTY_TYPE_MAP[property_type][1](**data)
