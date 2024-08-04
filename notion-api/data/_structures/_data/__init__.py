"""
The `_data` package is an internal package used to hide the implementation details of the data structures
used in the Notion API. It contains the data classes (DTOs) for validating various Notion API JSON payload
objects, ensuring that the data conforms to the expected structure and validation rules defined by the Notion API.

Purpose:
    - Define internal data models for various data structures used in the Notion API.
    - Ensure data integrity and consistency by validating the structure and types of the data.
    - Hide the implementation details from the public API to provide a cleaner and more user-friendly interface.

Implementation Details:
    - The package includes internal data models for various data structures, including files, icons, mentions,
      parents, text, and user-related structures.
    - Each data model is implemented as a Pydantic model, providing automatic validation and serialization.
    - The data models define the attributes and types for each object, ensuring that all required fields are present
      and correctly typed.

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

Note:
    This package is intended for internal use only to ensure that the data objects used in the Notion API are
    validated and structured correctly. It hides the implementation details from the public API, providing a cleaner
    and more user-friendly interface for developers.
"""
