"""
The `_factory` package is an internal package used to hide the implementation details of the factory methods
used for creating various Notion API JSON payload objects. It provides the logic for instantiating these objects,
ensuring they are created with the necessary attributes and validations.

Purpose:
    - Define internal factory methods for creating instances of various data structures used in the Notion API.
    - Simplify the instantiation process by encapsulating the creation logic within the factory methods.
    - Hide the implementation details from the public API to provide a cleaner and more user-friendly interface.

Implementation Details:
    - The package includes internal factory methods for various data structures, including files, icons, mentions,
      parents, text, and user-related structures.
    - Each factory method is designed to instantiate and return an object with default values and any necessary
      validations.
    - The factory methods leverage Pydantic models defined in the `_data` package to ensure data integrity and
      consistency.

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
    This package is intended for internal use only to simplify the creation of Notion API data structures. It hides
    the implementation details from the public API, providing a cleaner and more user-friendly interface for developers.
"""
