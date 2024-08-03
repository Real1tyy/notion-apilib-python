from DateProperty import DatePage, DateDatabase
from FormulaProperty import FormulaPage, FormulaDatabase
from NumberProperty import NumberPage, NumberDatabase, UniqueIdDatabase, UniqueIdPage
from PropertyType import PropertyType
from RelationProperty import RelationPage, RelationDatabase, RollupDatabase, RollupPage
from ResourcesProperty import EmailPage, FilesPage, PhoneNumberPage, FilesDatabase, EmailDatabase, \
    PhoneNumberDatabase, UrlDatabase, UrlPage
from SelectProperty import CheckboxPage, MultiSelectPage, CheckboxDatabase, MultiSelectDatabase, StatusDatabase, \
    StatusPage, SelectDatabase, SelectPage
from TextProperty import TitleDatabase, TitlePage, RichTextDatabase, RichTextPage
from TimeProperty import CreatedTimePage, LastEditedTimePage, CreatedTimeDatabase, LastEditedTimeDatabase
from UsersProperty import CreatedByPage, LastEditedByPage, PeoplePage, CreatedByDatabase, LastEditedByDatabase, \
    PeopleDatabase
from custom_types import json_

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
