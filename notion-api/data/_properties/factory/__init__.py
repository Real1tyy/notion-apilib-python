"""
This package, called `factory`, contains factory methods for creating various property objects
used in Notion API Page and Database Properties. These factory methods provide an easy and
consistent way to instantiate property objects with the necessary attributes, ensuring that they
are correctly structured and validated through Pydantic.

Purpose:
    - Provide factory methods to create instances of different property objects for Notion API.
    - Simplify the creation of property objects by encapsulating the necessary attributes and validations.

Modules included:
    - date: Contains factory methods for date properties.
    - formula: Contains factory methods for formula properties.
    - number: Contains factory methods for number and unique ID properties.
    - options: Contains factory methods for multi-select, select, status, and checkbox properties.
    - relation: Contains factory methods for relation and rollup properties.
    - resources: Contains factory methods for resource properties like email, files, phone number, and URL.
    - text: Contains factory methods for rich text and title properties.
    - time: Contains factory methods for time-related properties like created time and last edited time.
    - users: Contains factory methods for user-related properties like people, created by, and last edited by.

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

This package is not intended for direct use by end-users. Instead, it supports the higher-level
API provided by the main package, ensuring that all property objects are created consistently
and correctly.
"""

from _properties._factory.date import create_date_page, create_date_database
from _properties._factory.formula import create_formula_page, create_formula_database
from _properties._factory.number import create_number_page, create_unique_id_page, create_number_database, \
    create_unique_id_database
from _properties._factory.options import (
    create_multi_select_page, create_select_page, create_status_page,
    create_checkbox_page, create_select_database, create_multi_select_database,
    create_status_database, create_checkbox_database
)
from _properties._factory.relation import create_relation_page, create_rollup_page, create_relation_database, \
    create_rollup_database
from _properties._factory.resources import (
    create_email_page, create_files_page, create_phone_number_page, create_url_page,
    create_email_database, create_files_database, create_phone_number_database, create_url_database
)
from _properties._factory.text import create_rich_text_page, create_title_page, create_title_database, \
    create_rich_text_database
from _properties._factory.time import create_created_time_page, create_last_edited_time_page, \
    create_created_time_database, create_last_edited_time_database
from _properties._factory.users import create_people_page, create_created_by_page, create_last_edited_by_page, \
    create_people_database, create_created_by_database, create_last_edited_by_database

__all__ = [
    'create_date_page',
    'create_formula_page',
    'create_number_page',
    'create_unique_id_page',
    'create_multi_select_page',
    'create_select_page',
    'create_status_page',
    'create_checkbox_page',
    'create_relation_page',
    'create_rollup_page',
    'create_email_page',
    'create_files_page',
    'create_phone_number_page',
    'create_url_page',
    'create_rich_text_page',
    'create_title_page',
    'create_created_time_page',
    'create_last_edited_time_page',
    'create_people_page',
    'create_created_by_page',
    'create_last_edited_by_page',
    'create_date_database',
    'create_formula_database',
    'create_number_database',
    'create_unique_id_database',
    'create_select_database',
    'create_multi_select_database',
    'create_status_database',
    'create_checkbox_database',
    'create_relation_database',
    'create_rollup_database',
    'create_email_database',
    'create_files_database',
    'create_phone_number_database',
    'create_url_database',
    'create_rich_text_database',
    'create_title_database',
    'create_created_time_database',
    'create_last_edited_time_database',
    'create_people_database',
    'create_created_by_database',
    'create_last_edited_by_database'
]
