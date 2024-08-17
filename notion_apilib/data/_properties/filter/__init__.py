"""
This module provides various filter classes and factory methods for creating filters used in the Notion API.

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
"""

from .date_ import (
    DateFilter,
    create_concrete_date_filter,
    create_date_filter_is_empty,
    create_relative_date_filter,
)
from .formula_ import (
    FormulaFilter,
    create_formula_checkbox_filter,
    create_formula_date_filter,
    create_formula_number_filter,
    create_formula_string_filter,
)
from ._general import Filter, FilterStructure
from .number_ import (
    NumberFilter,
    create_concrete_number_filter,
    create_number_filter_is_empty,
    IDFilter,
    create_id_filter,
)
from .option_ import (
    MultiSelectFilter,
    create_multi_select_filter_contains,
    create_multi_select_filter_is_empty,
    CheckboxFilter,
    create_checkbox_filter,
    SelectFilter,
    create_select_filter_equals,
    create_select_filter_is_empty,
    create_multi_select_filter_does_not_contains,
    create_status_filter_equals,
    create_status_filter_does_not_equal,
    create_status_filter_is_empty,
    StatusFilter,
    create_select_filter_does_not_equal,
)
from .relation_ import (
    RelationFilter,
    create_relation_filter_contains,
    create_relation_filter_does_not_contain,
    create_relation_filter_is_empty,
    RelationFilter,
    create_rollup_filter,
)
from .resources_ import create_files_filter_is_empty, FilesFilter
from .text_ import (
    RichTextFilter,
    create_rich_text_filter,
    create_rich_text_filter_is_empty,
)
from .time_ import TimestampFilter, create_timestamp_filter
from .user_ import (
    PeopleFilter,
    create_people_filter_contains,
    create_people_filter_does_not_contain,
    create_people_filter_is_empty,
)
from .query_filter_ import AndFilter, OrFilter, QueryFilter

__all__ = [
    "DateFilter",
    "create_concrete_date_filter",
    "create_date_filter_is_empty",
    "create_relative_date_filter",
    "FormulaFilter",
    "create_formula_checkbox_filter",
    "create_formula_date_filter",
    "create_formula_number_filter",
    "create_formula_string_filter",
    "Filter",
    "FilterStructure",
    "NumberFilter",
    "create_concrete_number_filter",
    "create_number_filter_is_empty",
    "IDFilter",
    "create_id_filter",
    "MultiSelectFilter",
    "create_multi_select_filter_contains",
    "create_multi_select_filter_is_empty",
    "CheckboxFilter",
    "create_checkbox_filter",
    "SelectFilter",
    "create_select_filter_equals",
    "create_select_filter_is_empty",
    "create_multi_select_filter_does_not_contains",
    "create_status_filter_equals",
    "create_status_filter_does_not_equal",
    "create_status_filter_is_empty",
    "StatusFilter",
    "create_select_filter_does_not_equal",
    "RelationFilter",
    "create_relation_filter_contains",
    "create_relation_filter_does_not_contain",
    "create_relation_filter_is_empty",
    "create_rollup_filter",
    "create_files_filter_is_empty",
    "FilesFilter",
    "RichTextFilter",
    "create_rich_text_filter",
    "create_rich_text_filter_is_empty",
    "TimestampFilter",
    "create_timestamp_filter",
    "PeopleFilter",
    "create_people_filter_contains",
    "create_people_filter_does_not_contain",
    "create_people_filter_is_empty",
    "AndFilter",
    "OrFilter",
    "QueryFilter",
]
