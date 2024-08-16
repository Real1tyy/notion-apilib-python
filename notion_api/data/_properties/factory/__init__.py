"""
This package contains factory methods for creating various property objects
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
"""

# First Party
from notion_api.data._properties._factory.date import *
from notion_api.data._properties._factory.date import __all__ as date_all
from notion_api.data._properties._factory.formula import *
from notion_api.data._properties._factory.formula import __all__ as formula_all
from notion_api.data._properties._factory.number import *
from notion_api.data._properties._factory.number import __all__ as number_all
from notion_api.data._properties._factory.option import *
from notion_api.data._properties._factory.option import __all__ as option_all
from notion_api.data._properties._factory.relation import *
from notion_api.data._properties._factory.relation import __all__ as relation_all
from notion_api.data._properties._factory.resource import *
from notion_api.data._properties._factory.resource import __all__ as resource_all
from notion_api.data._properties._factory.text import *
from notion_api.data._properties._factory.text import __all__ as text_all
from notion_api.data._properties._factory.time import *
from notion_api.data._properties._factory.time import __all__ as time_all
from notion_api.data._properties._factory.user import *
from notion_api.data._properties._factory.user import __all__ as user_all

__all__ = (date_all + formula_all + number_all + option_all + relation_all + resource_all + text_all +
           time_all + user_all)
