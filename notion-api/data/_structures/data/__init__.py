"""
The `data` package inside the `structures` package contains data classes (DTOs) for validating various Notion API JSON
payload objects. These classes ensure that the data conforms to the expected structure and validation rules defined
by the Notion API.

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

Note:
    This package is intended for use by developers to ensure that the data objects used in the Notion API are
    validated and structured correctly. It provides a clear and structured representation of the data objects,
    facilitating data integrity and consistency.
"""

from .._data.file import *
from .._data.icon import *
from .._data.mention import *
from .._data.parent import *
from .._data.text import *
from .._data.user import *

__all__ = [
    'FileObject', 'External', 'FileAttributes', 'ResourcesAttributes',
    'Emoji', 'Icon',
    'Mention', 'DatabaseMention', 'DateMention', 'LinkPreviewMention', 'UserMention', 'TemplateMention',
    'TemplateMentionDate', 'TemplateMentionUser',
    'Parent',
    'RichText', 'Text', 'Link', 'Annotations',
    'User', 'OwnerStructure', 'PeopleStructure', 'People', 'BotStructure', 'Bot',
]
