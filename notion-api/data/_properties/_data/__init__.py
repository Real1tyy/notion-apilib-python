"""
The `_data` package contains the Pydantic data models for various property objects
used in Notion API Page and Database Properties. These data models define the structure
and validation rules for different types of properties, ensuring data integrity and
consistency when interacting with the Notion API.

Purpose:
    - Define the data models for Notion Page and Database Properties using Pydantic.
    - Enforce validation rules to ensure property objects adhere to the expected structure and data types.
    - Serve as the foundational layer for property objects, supporting the higher-level API provided
      by the main package.

Implementation Details:
    - The package includes data models for various property types, including date, formula, number,
      options (multi-select, select, status, checkbox), relation, rollup, resources (email, files,
      phone number, URL), text, time, and user-related properties.
    - Each data model is implemented as a Pydantic model, providing automatic validation and serialization.
    - The data models define the attributes and types for each property, ensuring that all required
      fields are present and correctly typed.

Modules Included:
    - date: Data models for date properties.
    - formula: Data models for formula properties.
    - number: Data models for number and unique ID properties.
    - option: Data models for multi-select, select, status, and checkbox properties.
    - relation: Data models for relation and rollup properties.
    - resources: Data models for resource properties like email, files, phone number, and URL.
    - text: Data models for rich text and title properties.
    - time: Data models for time-related properties like created time and last edited time.
    - users: Data models for user-related properties like people, created by, and last edited by.

Note:
    This package is intended for internal use within the library to define and validate
    the structure of property objects. It is not intended to be used directly by end-users.
"""
