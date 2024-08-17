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
from .date_ import DateDatabase, DatePage
from .formula_ import FormulaDatabase, FormulaPage
from .number_ import NumberPage, NumberDatabase, UniqueIdDatabase, UniqueIdPage
from .option_ import (
    MultiSelectPage,
    MultiSelectDatabase,
    SelectPage,
    SelectDatabase,
    CheckboxPage,
    CheckboxDatabase,
    StatusPage,
    StatusDatabase,
)
from .relation_ import RelationPage, RelationDatabase, RollupPage, RollupDatabase
from .resource_ import (
    FilesPage,
    FilesDatabase,
    EmailPage,
    EmailDatabase,
    PhoneNumberDatabase,
    PhoneNumberPage,
    UrlPage,
    UrlDatabase,
)
from .text_ import RichTextDatabase, RichTextPage, TitlePage, TitleDatabase
from .time_ import (
    CreatedTimePage,
    CreatedTimeDatabase,
    LastEditedTimePage,
    LastEditedTimeDatabase,
)
from .user_ import (
    CreatedByDatabase,
    CreatedByPage,
    LastEditedByPage,
    LastEditedByDatabase,
    PeopleDatabase,
    PeoplePage,
)

import notion_apilib.data._properties.data.structures as property_structures

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
