"""
This internal package contains the core implementation details for the Notion API Page and Database Properties.
It includes the data models and factory methods required to create and manage the properties of Notion pages and databases.

The classes and functions defined in this package are used internally by the interface package to provide a clean
and user-friendly API for interacting with Notion properties. These implementations are validated through Pydantic,
ensuring data integrity and consistency.

Purpose:
    - Define the data models for Notion Page and Database Properties.
    - Provide factory methods to create instances of these data models.
    - Validate the properties using Pydantic to maintain consistency and correctness.

Implementation Details:
    - The data models represent the structure of Notion properties such as text, numbers, dates, and more.
    - Factory methods are provided to create instances of these properties with default values and necessary validations.
    - This package is not intended to be used directly by end-users. Instead, it supports the interface package
      which exposes a simplified and user-friendly API.

Modules:
    - child: Contains data models and factory methods for child properties like pages and databases.
    - heading: Contains data models and factory methods for heading properties.
    - items: Contains data models and factory methods for list items such as to-do, bulleted, and numbered lists.
    - other: Contains data models and factory methods for other properties like callouts and synced _blocks.
    - tables: Contains data models and factory methods for table properties.
    - code: Contains data models and factory methods for code _blocks.
    - equation: Contains data models and factory methods for equation properties.
    - link: Contains data models and factory methods for link previews and bookmarks.
    - resources: Contains data models and factory methods for resource properties like files, images, videos, and PDFs.
    - text: Contains data models and factory methods for text properties.
    - time: Contains data models and factory methods for time-related properties like created time and last edited time.
    - users: Contains data models and factory methods for user-related properties like created by and last edited by.
"""
