"""
This package contains factory methods for creating various Notion API JSON
payload objects validated through Pydantic. These objects are used throughout the Notion API and include various data
structures that are not blocks or properties.

Purpose:
    - Provide factory methods to create instances of different data structures used in the Notion API.
    - Simplify the instantiation process for developers by offering pre-defined methods to create complex objects
      with minimal effort.
    - Ensure that the created objects adhere to the required structure and validation rules defined by the Notion API.

Implementation Details:
    - The package includes factory methods for various data structures, including files, icons, mentions, parents,
      text, and user-related structures.
    - Each factory method is designed to instantiate and return an object with default values and any necessary
      validations.
    - The factory methods leverage Pydantic models defined in the corresponding modules to ensure data integrity and
      consistency.

Factory Methods:
    - create_file_object
    - create_external
    - create_resources_attributes
    - create_file_attributes
    - create_icon
    - create_emoji
    - create_mention
    - create_template_mention_date
    - create_template_mention_user
    - create_template_mention
    - create_database_mention
    - create_date_mention
    - create_link_preview_mention
    - create_page_mention
    - create_user_mention
    - create_parent
    - create_parent_from_object
    - create_text
    - create_annotations
    - create_rich_text
    - create_link
    - create_basic_rich_text
    - create_basic_annotations
    - create_user
    - create_bot
    - create_people_structure
    - create_people
    - create_owner_structure
    - create_bot_structure
    - create_equation

Note:
    This package is intended for use by developers to simplify the creation of Notion API data structures. It provides
    factory methods that ensure all objects are created consistently and correctly, adhering to the Notion API's
    requirements.
"""

# First Party
from notion_api.data._structures._factory.file import *
from notion_api.data._structures._factory.file import __all__ as file_all
from notion_api.data._structures._factory.icon import *
from notion_api.data._structures._factory.icon import __all__ as icon_all
from notion_api.data._structures._factory.mention import *
from notion_api.data._structures._factory.mention import __all__ as mention_all
from notion_api.data._structures._factory.parent import *
from notion_api.data._structures._factory.parent import __all__ as parent_all
from notion_api.data._structures._factory.text import *
from notion_api.data._structures._factory.text import __all__ as text_all
from notion_api.data._structures._factory.user import *
from notion_api.data._structures._factory.user import __all__ as user_all

__all__ = file_all + icon_all + mention_all + parent_all + text_all + user_all
