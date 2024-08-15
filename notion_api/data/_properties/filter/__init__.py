"""
The `filter` package provides classes and factory methods for creating Filter objects used for querying a Notion Database through the API.

This package includes modules that define filter structures for various property types in Notion, such as date, number, text, relation, and more. Each module contains the necessary classes for representing filters and factory methods for creating these filters easily and consistently.

Modules available in this package:
- date: Handles filters for date properties.
- formula: Handles filters for formula-based properties.
- general: Provides general filter structures used by other specific filter types.
- number: Handles filters for number properties.
- option: Handles filters for select and multi-select properties.
- relation: Handles filters for relation properties.
- resources: Manages resources related to filters.
- text: Handles filters for text and rich text properties.
- user: Manages filters related to user properties like people, created_by, and last_edited_by.

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

- Filter
"""

from notion_api.data._properties._filter.date import *
from notion_api.data._properties._filter.formula import *
from notion_api.data._properties._filter.number import *
from notion_api.data._properties._filter.option import *
from notion_api.data._properties._filter.relation import *
from notion_api.data._properties._filter.resources import *
from notion_api.data._properties._filter.text import *
from notion_api.data._properties._filter.time import *
from notion_api.data._properties._filter.user import *
from notion_api.data._properties._filter.general import *

from notion_api.data._properties._filter.date import __all__ as __date_all__
from notion_api.data._properties._filter.formula import __all__ as __formula_all__
from notion_api.data._properties._filter.number import __all__ as __number_all__
from notion_api.data._properties._filter.option import __all__ as __option_all__
from notion_api.data._properties._filter.relation import __all__ as __relation_all__
from notion_api.data._properties._filter.resources import __all__ as __resources_all__
from notion_api.data._properties._filter.text import __all__ as __text_all__
from notion_api.data._properties._filter.time import __all__ as __time_all__
from notion_api.data._properties._filter.user import __all__ as __user_all__
from notion_api.data._properties._filter.general import __all__ as __general_all__

__all__ = (__date_all__ + __formula_all__ + __number_all__ + __option_all__ + __relation_all__ +
           __resources_all__ + __text_all__ + __time_all__ + __user_all__ + __general_all__)
