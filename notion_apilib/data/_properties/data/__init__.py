"""
This package, contains the Pydantic data models for various property objects
used in Notion API Page and Database Properties. These data models define the structure and
validation rules for different types of properties, ensuring data integrity and consistency
when interacting with the Notion API.

Purpose:
    - Define the data models for Notion Page and Database Properties using Pydantic.
    - Validate property objects to ensure they adhere to the expected structure and data types.
    - Support the higher-level API by providing validated property objects that can be used
      to interact with the Notion API.

Data Models:
    - DatePage
    - DateDatabase
    - FormulaPage
    - FormulaDatabase
    - NumberPage
    - NumberDatabase
    - UniqueIdPage
    - UniqueIdDatabase
    - MultiSelectPage
    - MultiSelectDatabase
    - SelectPage
    - SelectDatabase
    - CheckboxPage
    - CheckboxDatabase
    - StatusDatabase
    - StatusPage
    - RelationPage
    - RelationDatabase
    - RollupPage
    - RollupDatabase
    - FilesPage
    - FilesDatabase
    - EmailPage
    - EmailDatabase
    - PhoneNumberPage
    - PhoneNumberDatabase
    - UrlPage
    - UrlDatabase
    - RichTextPage
    - RichTextDatabase
    - TitlePage
    - TitleDatabase
    - CreatedTimePage
    - CreatedTimeDatabase
    - LastEditedTimePage
    - LastEditedTimeDatabase
    - CreatedByPage
    - CreatedByDatabase
    - LastEditedByPage
    - LastEditedByDatabase
    - PeoplePage
    - PeopleDatabase

- property_structures: Module that makes available to import all the low level Pydantic model data models for the
structures used inside the property objects.
"""

# First Party
import notion_apilib.data._properties.data.structures as property_structures

from .date_ import DateDatabase, DatePage
from .formula_ import FormulaDatabase, FormulaPage
from .number_ import NumberDatabase, NumberPage, UniqueIdDatabase, UniqueIdPage
from .option_ import (
    CheckboxDatabase,
    CheckboxPage,
    MultiSelectDatabase,
    MultiSelectPage,
    SelectDatabase,
    SelectPage,
    StatusDatabase,
    StatusPage,
)
from .relation_ import RelationDatabase, RelationPage, RollupDatabase, RollupPage
from .resource_ import (
    EmailDatabase,
    EmailPage,
    FilesDatabase,
    FilesPage,
    PhoneNumberDatabase,
    PhoneNumberPage,
    UrlDatabase,
    UrlPage,
)
from .text_ import RichTextDatabase, RichTextPage, TitleDatabase, TitlePage
from .time_ import CreatedTimeDatabase, CreatedTimePage, LastEditedTimeDatabase, LastEditedTimePage
from .user_ import CreatedByDatabase, CreatedByPage, LastEditedByDatabase, LastEditedByPage, PeopleDatabase, PeoplePage

__all__ = [
    "DateDatabase",
    "DatePage",
    "FormulaDatabase",
    "FormulaPage",
    "NumberPage",
    "NumberDatabase",
    "UniqueIdDatabase",
    "UniqueIdPage",
    "MultiSelectPage",
    "MultiSelectDatabase",
    "SelectPage",
    "SelectDatabase",
    "CheckboxPage",
    "CheckboxDatabase",
    "StatusPage",
    "StatusDatabase",
    "RelationPage",
    "RelationDatabase",
    "RollupPage",
    "RollupDatabase",
    "FilesPage",
    "FilesDatabase",
    "EmailPage",
    "EmailDatabase",
    "PhoneNumberDatabase",
    "PhoneNumberPage",
    "UrlPage",
    "UrlDatabase",
    "RichTextDatabase",
    "RichTextPage",
    "TitlePage",
    "TitleDatabase",
    "CreatedTimePage",
    "CreatedTimeDatabase",
    "LastEditedTimePage",
    "LastEditedTimeDatabase",
    "CreatedByDatabase",
    "CreatedByPage",
    "LastEditedByPage",
    "LastEditedByDatabase",
    "PeopleDatabase",
    "PeoplePage",
    "property_structures",
]
