"""
The package contains data classes (DTOs) for validating various Notion API JSON
payload objects through pydantic. These classes ensure that the data conforms to the expected structure and validation
rules defined by the Notion API.

Purpose:
    - Define data models for various data structures used in the Notion API.
    - Ensure data integrity and consistency by validating the structure and types of the data.
    - Provide a clear and structured representation of the data objects used in the Notion API.

Implementation Details:
    - The package includes data models for various data structures, including files, icons, mentions, parents,
      text, and user-related structures.
    - Each data model is implemented as a Pydantic model, providing automatic validation and serialization.
    - The data models define the attributes and types for each object, ensuring that all required fields are present
      and correctly typed.

Data Classes:
    - FileObject
    - External
    - FileAttributes
    - ResourcesAttributes
    - Emoji
    - Icon
    - Mention
    - DatabaseMention
    - DateMention
    - LinkPreviewMention
    - UserMention
    - TemplateMention
    - TemplateMentionDate
    - TemplateMentionUser
    - Parent
    - RichText
    - Text
    - Link
    - Annotations
    - User
    - OwnerStructure
    - PeopleStructure
    - People
    - BotStructure
    - Bot
    - Equation

Note:
    This package is intended for use by developers to ensure that the data objects used in the Notion API are
    validated and structured correctly. It provides a clear and structured representation of the data objects,
    facilitating data integrity and consistency.
"""

from _structures._data.file import *
from _structures._data.icon import *
from _structures._data.mention import *
from _structures._data.parent import *
from _structures._data.text import *
from _structures._data.user import *

from _structures._data.file import __all__ as file_all
from _structures._data.icon import __all__ as icon_all
from _structures._data.mention import __all__ as mention_all
from _structures._data.parent import __all__ as parent_all
from _structures._data.text import __all__ as text_all
from _structures._data.user import __all__ as user_all

FileAttributes.model_rebuild()
Icon.model_rebuild()
RichText.model_rebuild()

__all__ = file_all + icon_all + mention_all + parent_all + text_all + user_all
