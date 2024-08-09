"""
This package contains both the data classes and factory methods for validating and creating various
Notion API structures objects. This package provides a comprehensive set of tools to ensure that data
conforms to the expected structure and validation rules defined by the Notion API, and to simplify the creation of
these objects, enforced through Pydantic.

Purpose:
    - Define data models for various data structures used in the Notion API.
    - Ensure data integrity and consistency by validating the structure and types of the data.
    - Provide factory methods to create instances of different data structures used in the Notion API.

Implementation Details:
    - The package includes data models and factory methods for various data structures, including files, icons, mentions,
      parents, text, and user-related structures.
    - Each data model is implemented as a Pydantic model, providing automatic validation and serialization.
    - The data models define the attributes and types for each object, ensuring that all required fields are present
      and correctly typed.
    - Each factory method is designed to instantiate and return an object with default values and any necessary
      validations, leveraging the Pydantic models to ensure data integrity and consistency.

Data Classes:
    - FileObject: Represents a file object with a URL and expiry time.
    - External: Represents an external file with a URL.
    - FileAttributes: Represents attributes of a file including caption and name.
    - ResourcesAttributes: Represents attributes of a resource including type, external, and file.
    - Emoji: Represents an emoji with a type and value.
    - Icon: Represents an icon with a type, external, and file.
    - Mention: Represents a mention with various types like database, date, link preview, page, template, and user.
    - DatabaseMention: Represents a database mention with an ID.
    - DateMention: Represents a date mention with start and end times.
    - LinkPreviewMention: Represents a link preview mention with a URL.
    - UserMention: Represents a user mention with an object type and ID.
    - TemplateMention: Represents a template mention with date and user subtypes.
    - TemplateMentionDate: Represents a template mention date with a type and value.
    - TemplateMentionUser: Represents a template mention user with a type and value.
    - Parent: Represents a parent object with type and various ID fields.
    - RichText: Represents rich text with text, mention, equation, annotations, plain text, and href.
    - Text: Represents text content with optional links.
    - Link: Represents a link with a URL.
    - Annotations: Represents text annotations like bold, italic, strikethrough, underline, code, and color.
    - User: Represents a user with an object type, ID, and optional details like type, name, and avatar URL.
    - OwnerStructure: Represents the owner structure with a type.
    - PeopleStructure: Represents the structure of a person with an email.
    - People: Represents a person user with person structure details.
    - BotStructure: Represents the structure of a bot with an owner and workspace name.
    - Bot: Represents a bot user with bot structure details.

Factory Methods:
    - create_file_object: Creates a FileObject with URL and expiry time.
    - create_external: Creates an External file object with URL.
    - create_resources_attributes: Creates ResourcesAttributes with type, external, and file.
    - create_file_attributes: Creates FileAttributes with type, caption, name, external, and file.
    - create_icon: Creates an Icon with type, external, and file.
    - create_emoji: Creates an Emoji with type and value.
    - create_mention: Creates a Mention with various types like database, date, link preview, page, template, and user.
    - create_template_mention_date: Creates a TemplateMentionDate with type and value.
    - create_template_mention_user: Creates a TemplateMentionUser with type and value.
    - create_template_mention: Creates a TemplateMention with date and user subtypes.
    - create_database_mention: Creates a DatabaseMention with ID.
    - create_date_mention: Creates a DateMention with start and end times.
    - create_link_preview_mention: Creates a LinkPreviewMention with URL.
    - create_page_mention: Creates a PageMention with ID.
    - create_user_mention: Creates a UserMention with object type and ID.
    - create_parent: Creates a Parent object with type and various ID fields.
    - create_parent_from_object: Creates a Parent object from an existing object.
    - create_text: Creates a Text object with content and optional link.
    - create_annotations: Creates Annotations with bold, italic, strikethrough, underline, code, and color.
    - create_rich_text: Creates RichText with type, text, mention, equation, annotations, plain text, and href.
    - create_link: Creates a Link with URL.
    - create_basic_rich_text: Creates a basic RichText with minimal attributes.
    - create_basic_annotations: Creates basic Annotations with default values.
    - create_user: Creates a User with object type, ID, and optional details like type, name, and avatar URL.
    - create_bot: Creates a Bot with bot structure details.
    - create_people_structure: Creates a PeopleStructure with email.
    - create_people: Creates a People with person structure details.
    - create_owner_structure: Creates an OwnerStructure with type.
    - create_bot_structure: Creates a BotStructure with owner and workspace name.

Note:
    This package is intended for use by end-users to create and interact with Notion structure objects, which are all
    the low level properties of notion objects. It provides a user-friendly interface and ensures that all property
    objects are validated and structured correctly. The additional factory methods enable the transformation of JSON
    payloads from the Notion API into our custom DSL properties, facilitating seamless data integration.
"""

from data._structures.data import *
from data._structures.factory import *
from data._structures.types_ import *

from data._structures.data import __all__ as data_all
from data._structures.factory import __all__ as factory_all
from data._structures.types_ import __all__ as types_all

__all__ = data_all + factory_all + types_all
