"""
The `client` package provides the core components for interacting with the Notion API. This package contains provider classes responsible for managing communication with the Notion API, leveraging the Pydantic models defined in the data packages for validation and serialization.

### Purpose:
    - Facilitate seamless communication with the Notion API.
    - Manage the creation, retrieval, updating, and deletion of Notion objects such as blocks, pages, and databases.
    - Ensure that all API interactions conform to the expected structure and data integrity enforced by the Pydantic models.

### Components:

- **NotionBlockProvider**:
    Handles operations related to Notion blocks, allowing developers to create, update, retrieve, and delete blocks within their Notion workspace.

- **NotionPageProvider**:
    Manages interactions with Notion pages, including creating new pages, updating existing pages, and fetching page details from the API.

- **NotionDatabaseProvider**:
    Facilitates operations on Notion databases, such as creating databases, querying data, and managing database properties.

- **ResponseError**:
    A custom exception class used to handle and report errors that occur during API interactions, ensuring that issues are caught and managed gracefully.

### Integration:
This package is designed to work seamlessly with the Pydantic models defined in the `data` packages, ensuring that all API communications are validated and consistent with Notion's API schema. It abstracts the complexity of API calls, providing an intuitive interface for developers to interact with Notion objects.

### Key Features:
    - **API Abstraction**: Simplifies the process of communicating with the Notion API by providing high-level methods for common operations.
    - **Validation and Error Handling**: Ensures that all data sent to and received from the API is valid, and provides robust error handling to manage any issues that arise during API calls.
    - **Seamless Integration**: Works in tandem with the data models, ensuring consistency and integrity in all API interactions.

This package is essential for developers looking to manage their Notion workspace programmatically, offering a reliable and efficient way to interact with the Notion API.
"""

from .block_ import NotionBlockProvider
from .database_ import NotionDatabaseProvider
from .exceptions_ import ResponseError
from .page_ import NotionPageProvider

__all__ = [
    "NotionBlockProvider",
    "NotionPageProvider",
    "NotionDatabaseProvider",
    "ResponseError",
]
