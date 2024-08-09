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

    Data classes:
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

Note:
    This package is intended for use by end-users to create and interact with Notion property objects.
    It provides a user-friendly interface and ensures that all property objects are validated and structured
    correctly. The additional factory methods enable the transformation of JSON payloads from the Notion API
    into our custom DSL properties, facilitating seamless data integration.
"""

from structures import *

from data._properties.data import *
from data._properties.factory import *
from data._properties.property_factory import *
from data._properties.property import *

from data._properties.data import __all__ as data_all
from data._properties.factory import __all__ as factory_all
from data._properties.property_factory import __all__ as property_factory_all
from data._properties.property import __all__ as property_all

__all__ = data_all + factory_all + property_factory_all + property_all
