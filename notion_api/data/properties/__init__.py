"""
This package contains both the Page and Database Properties model objects for the Notion API, validated through
Pydantic. It serves as the interface
package that consolidates factory methods for creating properties and the data classes representing
the structure of Notion API Page and Database Properties.

The factory methods provide an easy way to create property objects with the necessary attributes,
while the data classes define the structure and validation of these properties using Pydantic.

Additionally, the package includes factory methods for transforming JSON data into our custom DSL models validated
through Pydantic. This feature allows users to seamlessly convert their JSON data into our structured and validated
classes.

__all__:
    Factory functions:
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

    Data classes - you can use the class method create_sort_object to get the desired sorting object for database
    querying:
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

    Factory:
        - create_concrete_page_property_type
        - create_concrete_database_property_type

    Generic Properties:
        - PageProperty
        - DatabaseProperty
        - PropertyType

    Sort Objects with static class factory methods used in database querying:
        - Sort
        - PropertySort
        - TimestampSort

    Generic Filter Object to create filters used for querying databases:
        - Filter
        - QueryFilterOptions
        - QueryFilter

    Concrete Filter Objects and their factory methods:
    - CheckboxFilter
      - `create_checkbox_filter_equals(property_name: str, equals: bool) -> CheckboxFilter`
      - `create_checkbox_filter_does_not_equal(property_name: str, does_not_equal: bool) -> CheckboxFilter`

    - DateFilter
      - `create_date_filter_is_empty(property_name: str, is_empty: bool) -> DateFilter`
      - `create_concrete_date_filter(property_name: str, filter_type: Literal['after', 'before', 'equals', 'on_or_after', 'on_or_before'], date_value: datetime) -> DateFilter`
      - `create_relative_date_filter(property_name: str, filter_type: Literal['next_month', 'next_week', 'next_year', 'past_month', 'past_week', 'past_year', 'this_week']) -> DateFilter`

    - FilesFilter (Assumed class and methods, adjust if necessary)
      - `create_files_filter_contains(property_name: str, contains: str) -> FilesFilter`
      - `create_files_filter_does_not_contain(property_name: str, does_not_contain: str) -> FilesFilter`

    - FormulaFilter
      - `create_formula_checkbox_filter(property_name: str, checkbox_filter: dict) -> FormulaFilter`
      - `create_formula_date_filter(property_name: str, date_filter: dict) -> FormulaFilter`
      - `create_formula_number_filter(property_name: str, number_filter: dict) -> FormulaFilter`
      - `create_formula_string_filter(property_name: str, string_filter: dict) -> FormulaFilter`

    - MultiSelectFilter
      - `create_multi_select_filter_contains(property_name: str, contains: str) -> MultiSelectFilter`
      - `create_multi_select_filter_is_empty(property_name: str, is_empty: bool) -> MultiSelectFilter`

    - NumberFilter
      - `create_number_filter_is_empty(property_name: str, is_empty: bool) -> NumberFilter`
      - `create_concrete_number_filter(property_name: str, filter_type: Literal['does_not_equal', 'equals', 'greater_than', 'greater_than_or_equal_to', 'less_than', 'less_than_or_equal_to'], number_value: float) -> NumberFilter`

    - PeopleFilter
      - `create_people_filter_contains(property_name: str, contains: str) -> PeopleFilter`
      - `create_people_filter_does_not_contain(property_name: str, does_not_contain: str) -> PeopleFilter`
      - `create_people_filter_is_empty(property_name: str, is_empty: bool) -> PeopleFilter`

    - PhoneNumberFilter (Assumed class and methods, adjust if necessary)
      - `create_phone_number_filter_contains(property_name: str, contains: str) -> PhoneNumberFilter`
      - `create_phone_number_filter_does_not_contain(property_name: str, does_not_contain: str) -> PhoneNumberFilter`
      - `create_phone_number_filter_is_empty(property_name: str, is_empty: bool) -> PhoneNumberFilter`

    - RelationFilter
      - `create_relation_filter_contains(property_name: str, contains: str) -> RelationFilter`
      - `create_relation_filter_does_not_contain(property_name: str, does_not_contain: str) -> RelationFilter`
      - `create_relation_filter_is_empty(property_name: str, is_empty: bool) -> RelationFilter`

    - RichTextFilter
      - `create_rich_text_filter(property_name: str, filter_type: Literal['contains', 'does_not_contain', 'does_not_equal', 'ends_with', 'equals', 'starts_with', 'is_empty', 'is_not_empty'], text_value: Optional[str] = None) -> RichTextFilter`

    - SelectFilter
      - `create_select_filter_equals(property_name: str, equals: str) -> SelectFilter`
      - `create_select_filter_does_not_equal(property_name: str, does_not_equal: str) -> SelectFilter`
      - `create_select_filter_is_empty(property_name: str, is_empty: bool) -> SelectFilter`

    - StatusFilter
      - `create_status_filter_equals(property_name: str, equals: str) -> StatusFilter`
      - `create_status_filter_does_not_equal(property_name: str, does_not_equal: str) -> StatusFilter`
      - `create_status_filter_is_empty(property_name: str, is_empty: bool) -> StatusFilter`

    - TimestampFilter
      - `create_timestamp_filter(timestamp_type: Literal['created_time', 'last_edited_time'], date_filter: DateFilter) -> TimestampFilter`

    - IDFilter
      - `create_id_filter(property_name: str, filter_type: Literal['equals', 'does_not_equal', 'greater_than', 'greater_than_or_equal_to', 'less_than', 'less_than_or_equal_to'], value: int) -> IDFilter`
"""

from notion_api.data.structures import *

from notion_api.data._properties.data import *
from notion_api.data._properties.factory import *
from notion_api.data._properties.property_factory import *
from notion_api.data._properties.property import *
from notion_api.data._properties.sort import *
from notion_api.data._properties.filter import *
from notion_api.data._properties.query_filter import *

from notion_api.data._properties.data import __all__ as data_all
from notion_api.data._properties.factory import __all__ as factory_all
from notion_api.data._properties.property_factory import __all__ as property_factory_all
from notion_api.data._properties.property import __all__ as property_all
from notion_api.data._properties.sort import __all__ as sort_all
from notion_api.data._properties.filter import __all__ as filter_all
from notion_api.data._properties.query_filter import __all__ as query_filter_all

__all__ = data_all + factory_all + property_factory_all + property_all + sort_all + filter_all + query_filter_all
