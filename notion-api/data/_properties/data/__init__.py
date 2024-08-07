"""
This package, called `data`, contains the Pydantic data models for various property objects
used in Notion API Page and Database Properties. These data models define the structure and
validation rules for different types of properties, ensuring data integrity and consistency
when interacting with the Notion API.

Purpose:
    - Define the data models for Notion Page and Database Properties using Pydantic.
    - Validate property objects to ensure they adhere to the expected structure and data types.
    - Support the higher-level API by providing validated property objects that can be used
      to interact with the Notion API.

Modules included:
    - date: Contains data models for date properties.
    - formula: Contains data models for formula properties.
    - number: Contains data models for number and unique ID properties.
    - option: Contains data models for multi-select, select, status, and checkbox properties.
    - relation: Contains data models for relation and rollup properties.
    - resources: Contains data models for resource properties like email, files, phone number, and URL.
    - text: Contains data models for rich text and title properties.
    - time: Contains data models for time-related properties like created time and last edited time.
    - users: Contains data models for user-related properties like people, created by, and last edited by.

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

This package is not intended for direct use by end-users. Instead, it supports the higher-level
API provided by the main package, ensuring that all property objects are validated and structured
correctly.
"""

from _properties._data.date import *
from _properties._data.formula import *
from _properties._data.number import *
from _properties._data.option import *
from _properties._data.relation import *
from _properties._data.resource import *
from _properties._data.text import *
from _properties._data.time import *
from _properties._data.user import *

from _properties._data.date import __all__ as date
from _properties._data.formula import __all__ as formula
from _properties._data.number import __all__ as number
from _properties._data.option import __all__ as option
from _properties._data.relation import __all__ as relation
from _properties._data.resource import __all__ as resources
from _properties._data.text import __all__ as text
from _properties._data.time import __all__ as time
from _properties._data.user import __all__ as users

__all__ = date + formula + number + option + relation + resources + text + time + users
