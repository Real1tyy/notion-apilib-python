"""
The package contains pydantic model classes for validating various Notion API JSON
payload objects through Pydantic. These classes ensure that the data conforms to the expected structure and validation
rules defined by the Notion API. This class is used inside other Notion API classes to validate the data structure
that is used multiple times to reduce duplication and promote reuse.

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
    - PageMention
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
    - EquationStructure

Note:
    This package is intended for use by developers to ensure that the data objects used in the Notion API are
    validated and structured correctly. It provides a clear and structured representation of the data objects,
    facilitating data integrity and consistency.
"""

from .file_ import External, FileAttributes, FileObject, ResourcesAttributes
from .icon_ import Emoji
from .mention_ import (
    DatabaseMention,
    DateMention,
    LinkPreviewMention,
    Mention,
    PageMention,
    TemplateMention,
    TemplateMentionDate,
    TemplateMentionUser,
    UserMention,
)
from .parent_ import Parent
from .text_ import Annotations, EquationStructure, FormatedText, Link, RichText, Text
from .user_ import Bot, BotStructure, OwnerStructure, People, PeopleStructure, User

__all__ = [
    "FileObject",
    "External",
    "FileAttributes",
    "ResourcesAttributes",
    "Emoji",
    "Mention",
    "DatabaseMention",
    "DateMention",
    "LinkPreviewMention",
    "UserMention",
    "TemplateMention",
    "TemplateMentionDate",
    "TemplateMentionUser",
    "PageMention",
    "Parent",
    "RichText",
    "Text",
    "FormatedText",
    "Link",
    "Annotations",
    "EquationStructure",
    "User",
    "OwnerStructure",
    "PeopleStructure",
    "People",
    "BotStructure",
    "Bot",
]
