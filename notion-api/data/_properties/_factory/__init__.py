"""
The `_factory` package contains factory methods for creating various property objects
used in Notion API Page and Database Properties. These factory methods ensure that
the property objects are instantiated with the necessary attributes and validations,
streamlining the process of creating consistent and correctly structured objects.

Purpose:
    - Provide factory methods to create instances of different property objects for the Notion API.
    - Encapsulate the creation logic for property objects, ensuring that they are created with
      all required attributes and adhere to the expected structure.
    - Simplify the instantiation process for developers by offering pre-defined methods to create
      complex property objects with minimal effort.

Implementation Details:
    - The package includes factory methods for various property types, including date, formula,
      number, options (multi-select, select, status, checkbox), relation, rollup, resources (email,
      files, phone number, URL), text, time, and user-related properties.
    - Each factory method is designed to instantiate and return a property object with default
      values and any necessary validations.
    - The factory methods leverage Pydantic models defined in the `_data` package to ensure data
      integrity and consistency.

Modules Included:
    - date: Factory methods for date properties.
    - formula: Factory methods for formula properties.
    - number: Factory methods for number and unique ID properties.
    - options: Factory methods for multi-select, select, status, and checkbox properties.
    - relation: Factory methods for relation and rollup properties.
    - resources: Factory methods for resource properties like email, files, phone number, and URL.
    - text: Factory methods for rich text and title properties.
    - time: Factory methods for time-related properties like created time and last edited time.
    - users: Factory methods for user-related properties like people, created by, and last edited by.

Note:
    This package is intended for internal use within the library to support the creation
    of property objects. It is not intended to be used directly by end-users.
"""
