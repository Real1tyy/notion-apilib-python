"""
This package contains factory methods for creating various property objects used in Notion API Page and Database Properties.
These factory methods provide an easy and consistent way to instantiate property objects with the necessary attributes,
ensuring that they are correctly structured and validated through Pydantic.

Purpose:
    - Provide factory methods to create instances of different property objects for the Notion API.
    - Simplify the creation of property objects by encapsulating the necessary attributes and validations.

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
from .date_ import create_date_database, create_date_page
from .formula_ import create_formula_page, create_formula_database
from .number_ import (
    create_number_page,
    create_number_database,
    create_unique_id_page,
    create_unique_id_database,
)
from .option_ import (
    create_select_page,
    create_status_page,
    create_checkbox_page,
    create_checkbox_database,
    create_status_database,
    create_select_database,
    create_multi_select_database,
    create_multi_select_page,
)
from .relation_ import (
    create_relation_page,
    create_rollup_page,
    create_relation_database,
    create_rollup_database,
)
from .resource_ import (
    create_url_page,
    create_email_page,
    create_files_page,
    create_url_database,
    create_email_database,
    create_files_database,
    create_phone_number_database,
    create_phone_number_page,
)
from .text_ import (
    create_rich_text_page,
    create_title_page,
    create_title_database,
    create_rich_text_database,
)
from .time_ import (
    create_created_time_page,
    create_created_time_database,
    create_last_edited_time_page,
    create_last_edited_time_database,
)
from .user_ import (
    create_people_page,
    create_created_by_page,
    create_people_database,
    create_created_by_database,
    create_last_edited_by_database,
    create_last_edited_by_page,
)

__all__ = [
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
]
