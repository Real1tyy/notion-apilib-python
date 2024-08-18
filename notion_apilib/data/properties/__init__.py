"""
This package provides comprehensive tools for interacting with the Notion API, specifically focusing on property objects,
data models, and related utilities used in Notion API Page and Database Properties. The package includes:

1. **Pydantic Data Models**:
   - Data models that define the structure and validation rules for various property types in Notion Page and Database Properties.
   - These models ensure data integrity and consistency when interacting with the Notion API.

2. **Factory Methods**:
   - Factory methods for creating various property objects with the necessary attributes.
   - These methods provide an easy and consistent way to instantiate property objects, ensuring they are correctly structured and validated.

3. **Utility Functions**:
   - Functions for deserializing properties and creating sort objects, enabling more advanced manipulation of Notion data.

Purpose:
    - Define and validate data models for Notion Page and Database Properties using Pydantic.
    - Provide factory methods to simplify the creation of property objects.
    - Offer utility functions to support advanced interactions with Notion data.

Implementation Details:
    - The package includes data models, factory methods, and utility functions for various property types,
      including date, formula, number, option, relation, resource, text, time, and user properties.
    - Each model and factory method is designed to ensure data integrity, consistency, and ease of use when interacting with the Notion API.

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

Factory Methods:
    - create_date_page
    - create_formula_page
    - create_number_page
    - create_unique_id_page
    - create_multi_select_page
    - create_select_page
    - create_status_page
    - create_checkbox_page
    - create_relation_page
    - create_rollup_page
    - create_email_page
    - create_files_page
    - create_phone_number_page
    - create_url_page
    - create_rich_text_page
    - create_title_page
    - create_created_time_page
    - create_last_edited_time_page
    - create_people_page
    - create_created_by_page
    - create_last_edited_by_page
    - create_date_database
    - create_formula_database
    - create_number_database
    - create_unique_id_database
    - create_select_database
    - create_multi_select_database
    - create_status_database
    - create_checkbox_database
    - create_relation_database
    - create_rollup_database
    - create_email_database
    - create_files_database
    - create_phone_number_database
    - create_url_database
    - create_rich_text_database
    - create_title_database
    - create_created_time_database
    - create_last_edited_time_database
    - create_people_database
    - create_created_by_database
    - create_last_edited_by_database

Filters:
    Filter Classes:
        - DateFilter: Handles date-related filters.
        - FormulaFilter: Handles formula-related filters.
        - Filter: Base class for all filters.
        - FilterStructure: Structure for filters.
        - NumberFilter: Handles number-related filters.
        - IDFilter: Handles ID-related filters.
        - MultiSelectFilter: Handles multi-select filters.
        - CheckboxFilter: Handles checkbox filters.
        - SelectFilter: Handles select filters.
        - StatusFilter: Handles status filters.
        - RelationFilter: Handles relation filters.
        - FilesFilter: Handles file-related filters.
        - RichTextFilter: Handles rich text filters.
        - TimestampFilter: Handles timestamp filters.
        - PeopleFilter: Handles people-related filters.
        - AndFilter: Handles AND logic for combining filters.
        - OrFilter: Handles OR logic for combining filters.
        - QueryFilter: Base class for query filters.

    Factory Methods:
        - create_concrete_date_filter: Creates a concrete date filter.
        - create_date_filter_is_empty: Creates a date filter for empty values.
        - create_relative_date_filter: Creates a relative date filter.
        - create_formula_checkbox_filter: Creates a formula checkbox filter.
        - create_formula_date_filter: Creates a formula date filter.
        - create_formula_number_filter: Creates a formula number filter.
        - create_formula_string_filter: Creates a formula string filter.
        - create_concrete_number_filter: Creates a concrete number filter.
        - create_number_filter_is_empty: Creates a number filter for empty values.
        - create_id_filter: Creates an ID filter.
        - create_multi_select_filter_contains: Creates a multi-select filter for containing values.
        - create_multi_select_filter_is_empty: Creates a multi-select filter for empty values.
        - create_checkbox_filter: Creates a checkbox filter.
        - create_select_filter_equals: Creates a select filter for equal values.
        - create_select_filter_is_empty: Creates a select filter for empty values.
        - create_multi_select_filter_does_not_contains: Creates a multi-select filter for not containing values.
        - create_status_filter_equals: Creates a status filter for equal values.
        - create_status_filter_does_not_equal: Creates a status filter for not equal values.
        - create_status_filter_is_empty: Creates a status filter for empty values.
        - create_select_filter_does_not_equal: Creates a select filter for not equal values.
        - create_relation_filter_contains: Creates a relation filter for containing values.
        - create_relation_filter_does_not_contain: Creates a relation filter for not containing values.
        - create_relation_filter_is_empty: Creates a relation filter for empty values.
        - create_rollup_filter: Creates a rollup filter.
        - create_files_filter_is_empty: Creates a file filter for empty values.
        - create_rich_text_filter: Creates a rich text filter.
        - create_rich_text_filter_is_empty: Creates a rich text filter for empty values.
        - create_timestamp_filter: Creates a timestamp filter.
        - create_people_filter_contains: Creates a people filter for containing values.
        - create_people_filter_does_not_contain: Creates a people filter for not containing values.
        - create_people_filter_is_empty: Creates a people filter for empty values.

    - Filter Objects:
        - AndFilter
        - OrFilter
        - QueryFilter

- Utility Functions for JSON Deserialization of Properties:
    "deserialize_page_property",
    "deserialize_database_property",

- Factory Methods for Creating Sort Objects and Sort Object types:
    "created_sort_object",
    "create_created_time_sort",
    "create_last_edited_time_sort",
    "Sort",
    "PropertySort",
    "TimestampSort",

- Properties Abstract Classes:
    "Property",
    "PageProperty",
    "DatabaseProperty",
    "PropertyType",

"""

# First Party
import notion_apilib.data._properties.filter as property_filter
from notion_apilib.data._properties.data import (
    CheckboxDatabase,
    CheckboxPage,
    CreatedByDatabase,
    CreatedByPage,
    CreatedTimeDatabase,
    CreatedTimePage,
    DateDatabase,
    DatePage,
    EmailDatabase,
    EmailPage,
    FilesDatabase,
    FilesPage,
    FormulaDatabase,
    FormulaPage,
    LastEditedByDatabase,
    LastEditedByPage,
    LastEditedTimeDatabase,
    LastEditedTimePage,
    MultiSelectDatabase,
    MultiSelectPage,
    NumberDatabase,
    NumberPage,
    PeopleDatabase,
    PeoplePage,
    PhoneNumberDatabase,
    PhoneNumberPage,
    RelationDatabase,
    RelationPage,
    RichTextDatabase,
    RichTextPage,
    RollupDatabase,
    RollupPage,
    SelectDatabase,
    SelectPage,
    StatusDatabase,
    StatusPage,
    TitleDatabase,
    TitlePage,
    UniqueIdDatabase,
    UniqueIdPage,
    UrlDatabase,
    UrlPage,
)
from notion_apilib.data._properties.factory import (
    create_checkbox_database,
    create_checkbox_page,
    create_created_by_database,
    create_created_by_page,
    create_created_time_database,
    create_created_time_page,
    create_date_database,
    create_date_page,
    create_email_database,
    create_email_page,
    create_files_database,
    create_files_page,
    create_formula_database,
    create_formula_page,
    create_last_edited_by_database,
    create_last_edited_by_page,
    create_last_edited_time_database,
    create_last_edited_time_page,
    create_multi_select_database,
    create_multi_select_page,
    create_number_database,
    create_number_page,
    create_people_database,
    create_people_page,
    create_phone_number_database,
    create_phone_number_page,
    create_relation_database,
    create_relation_page,
    create_rich_text_database,
    create_rich_text_page,
    create_rollup_database,
    create_rollup_page,
    create_select_database,
    create_select_page,
    create_status_database,
    create_status_page,
    create_title_database,
    create_title_page,
    create_unique_id_database,
    create_unique_id_page,
    create_url_database,
    create_url_page,
)
from notion_apilib.data._properties.filter import (
    AndFilter,
    CheckboxFilter,
    DateFilter,
    FilesFilter,
    Filter,
    FilterStructure,
    FormulaFilter,
    IDFilter,
    MultiSelectFilter,
    NumberFilter,
    OrFilter,
    PeopleFilter,
    QueryFilter,
    RelationFilter,
    RichTextFilter,
    SelectFilter,
    StatusFilter,
    TimestampFilter,
    create_checkbox_filter,
    create_concrete_date_filter,
    create_concrete_number_filter,
    create_date_filter_is_empty,
    create_files_filter_is_empty,
    create_formula_checkbox_filter,
    create_formula_date_filter,
    create_formula_number_filter,
    create_formula_string_filter,
    create_id_filter,
    create_multi_select_filter_contains,
    create_multi_select_filter_does_not_contains,
    create_multi_select_filter_is_empty,
    create_number_filter_is_empty,
    create_people_filter_contains,
    create_people_filter_does_not_contain,
    create_people_filter_is_empty,
    create_relation_filter_contains,
    create_relation_filter_does_not_contain,
    create_relation_filter_is_empty,
    create_relative_date_filter,
    create_rich_text_filter,
    create_rich_text_filter_is_empty,
    create_rollup_filter,
    create_select_filter_does_not_equal,
    create_select_filter_equals,
    create_select_filter_is_empty,
    create_status_filter_does_not_equal,
    create_status_filter_equals,
    create_status_filter_is_empty,
    create_timestamp_filter,
)
from notion_apilib.data._properties.property import DatabaseProperty, PageProperty, Property, PropertyType
from notion_apilib.data._properties.property_factory import deserialize_database_property, deserialize_page_property
from notion_apilib.data._properties.sort_ import (
    PropertySort,
    Sort,
    TimestampSort,
    create_created_time_sort,
    create_last_edited_time_sort,
    created_sort_object,
)

__all__ = [
    # Data Models
    "DatePage",
    "DateDatabase",
    "FormulaPage",
    "FormulaDatabase",
    "NumberPage",
    "NumberDatabase",
    "UniqueIdPage",
    "UniqueIdDatabase",
    "MultiSelectPage",
    "MultiSelectDatabase",
    "SelectPage",
    "SelectDatabase",
    "CheckboxPage",
    "CheckboxDatabase",
    "StatusDatabase",
    "StatusPage",
    "RelationPage",
    "RelationDatabase",
    "RollupPage",
    "RollupDatabase",
    "FilesPage",
    "FilesDatabase",
    "EmailPage",
    "EmailDatabase",
    "PhoneNumberPage",
    "PhoneNumberDatabase",
    "UrlPage",
    "UrlDatabase",
    "RichTextPage",
    "RichTextDatabase",
    "TitlePage",
    "TitleDatabase",
    "CreatedTimePage",
    "CreatedTimeDatabase",
    "LastEditedTimePage",
    "LastEditedTimeDatabase",
    "CreatedByPage",
    "CreatedByDatabase",
    "LastEditedByPage",
    "LastEditedByDatabase",
    "PeoplePage",
    "PeopleDatabase",
    # Factory Methods
    "create_date_page",
    "create_formula_page",
    "create_number_page",
    "create_unique_id_page",
    "create_multi_select_page",
    "create_select_page",
    "create_status_page",
    "create_checkbox_page",
    "create_relation_page",
    "create_rollup_page",
    "create_email_page",
    "create_files_page",
    "create_phone_number_page",
    "create_url_page",
    "create_rich_text_page",
    "create_title_page",
    "create_created_time_page",
    "create_last_edited_time_page",
    "create_people_page",
    "create_created_by_page",
    "create_last_edited_by_page",
    "create_date_database",
    "create_formula_database",
    "create_number_database",
    "create_unique_id_database",
    "create_select_database",
    "create_multi_select_database",
    "create_status_database",
    "create_checkbox_database",
    "create_relation_database",
    "create_rollup_database",
    "create_email_database",
    "create_files_database",
    "create_phone_number_database",
    "create_url_database",
    "create_rich_text_database",
    "create_title_database",
    "create_created_time_database",
    "create_last_edited_time_database",
    "create_people_database",
    "create_created_by_database",
    "create_last_edited_by_database",
    # Utility Functions
    "deserialize_page_property",
    "deserialize_database_property",
    "created_sort_object",
    "create_created_time_sort",
    "create_last_edited_time_sort",
    # Properties
    "PageProperty",
    "DatabaseProperty",
    "PropertyType",
    "Property",
    # Sorts
    "Sort",
    "PropertySort",
    "TimestampSort",
    # Filters
    "property_filter",
    "DateFilter",
    "FormulaFilter",
    "Filter",
    "FilterStructure",
    "NumberFilter",
    "IDFilter",
    "MultiSelectFilter",
    "CheckboxFilter",
    "SelectFilter",
    "StatusFilter",
    "RelationFilter",
    "FilesFilter",
    "RichTextFilter",
    "TimestampFilter",
    "PeopleFilter",
    "AndFilter",
    "OrFilter",
    "QueryFilter",
    "create_concrete_date_filter",
    "create_date_filter_is_empty",
    "create_relative_date_filter",
    "create_formula_checkbox_filter",
    "create_formula_date_filter",
    "create_formula_number_filter",
    "create_formula_string_filter",
    "create_concrete_number_filter",
    "create_number_filter_is_empty",
    "create_id_filter",
    "create_multi_select_filter_contains",
    "create_multi_select_filter_is_empty",
    "create_checkbox_filter",
    "create_select_filter_equals",
    "create_select_filter_is_empty",
    "create_multi_select_filter_does_not_contains",
    "create_status_filter_equals",
    "create_status_filter_does_not_equal",
    "create_status_filter_is_empty",
    "create_select_filter_does_not_equal",
    "create_relation_filter_contains",
    "create_relation_filter_does_not_contain",
    "create_relation_filter_is_empty",
    "create_rollup_filter",
    "create_files_filter_is_empty",
    "create_rich_text_filter",
    "create_rich_text_filter_is_empty",
    "create_timestamp_filter",
    "create_people_filter_contains",
    "create_people_filter_does_not_contain",
    "create_people_filter_is_empty",
]
