"""
This  package provides a robust set of Python classes, factory methods, and validation mechanisms to interface with
the Notion API. This package abstracts the complex Notion API structure into an intuitive, custom Domain-Specific Language (DSL), allowing developers to easily create, manipulate, and validate Notion objects without needing to know the underlying API details.

### Inner Packages Overview:

- **blocks**:
    Contains classes representing all types of Notion blocks. Blocks are the fundamental building units in Notion, such as paragraphs, headings, lists, and more. Each block class is designed to mirror the Notion API schema, with attributes that conform to the API's structure. Pydantic is used for data validation, ensuring that the blocks adhere to Notion's requirements. Factory methods are provided to facilitate the creation of these blocks, making it easy to instantiate and manipulate them within your Notion workspace.

- **structures**:
    This module houses low-level structure objects that are used repeatedly throughout the Notion API but don't hold standalone significance. These are the fundamental components such as `RichText`, `Annotations`, and other similar entities that appear within blocks and properties. They serve as building blocks for more complex structures and are essential for creating valid Notion API objects. Like other modules, these objects are validated using Pydantic and come with factory methods to simplify their creation.

- **properties**:
    This module includes classes for page and database properties, as well as the `Page` and `Database` objects themselves. The property classes encapsulate all possible attributes a Notion page or database can have, such as titles, dates, select options, and more. The `Page` and `Database` classes provide an easy interface to create and manipulate entire pages or databases within Notion, abstracting away the complexity of dealing with the raw API. These classes are also Pydantic-validated and supported by factory methods for quick instantiation.


data classes provided:
    - Page
    - Database
    - PageProperties
    - DatabaseProperties
factory methods to deserialize json into our DSL data class:
    - create_page
    - create_database



### Key Features:
- **Schema Enforcement**: All classes enforce schema rules using Pydantic, ensuring that the data conforms to Notion's API structure before being sent or processed.
- **Factory Methods**: Each module provides factory methods for easy instantiation of objects, reducing the need for manual configuration and lowering the learning curve for developers.
- **Custom DSL**: By abstracting the Notion API structure, this package allows developers to interact with Notion using a Pythonic interface, making code more readable and maintainable.

This package is essential for developers who want to interact with the Notion API without getting bogged down in its intricacies, providing a more intuitive and error-resistant way to build and manipulate Notion objects.
"""
from notion_api.data.structures import *

from notion_api.data.page import *
from notion_api.data.database import *

from notion_api.data.page import __all__ as page_all
from notion_api.data.database import __all__ as database_all

__all__ = page_all + database_all
