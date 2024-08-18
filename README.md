# notion-apilib-python

This library allows developers to work with Notion API using custom DSL Pydantic models, removing the need to manually
construct json payloads and API requests or handle JSON responses. The library wraps the Notion REST API, transforming
the calls into intuitive custom API methods that accept and return custom Pydantic objects. Also provides factory
methods
for easy instantiation of these custom objects.

## Key Features

- Schema Enforcement: Ensures data integrity by validating all objects against Notion's API schema using Pydantic.
- Factory Methods: Simplifies the creation of Notion objects with pre-configured factory methods.
- Provide a high-level abstraction over Notion's REST API. Abstracting away the low-level details of the API like json
  structure, formats and URL's.
- Simple and intuitive syntax for creating, retrieving, updating, and deleting Notion objects like Pages, Databases
  and Blocks.
- Supports pagination, filtering, sorting, and other advanced features.

## Installation

You can install the package via pip, link to the package -
[PyPi Package](https://pypi.org/project/notion-apilib/)

```bash
pip install notion-apilib
```

## Usage

```python
from notion_apilib import NotionApi

# Initialize the client
client = NotionApi(api_key="your_notion_integration_secret_api_key")

# Access the notion object providers / accessors:
page_provider = client.page_provider
blocks_provider = client.block_provider
database_provider = client.database_provider

# Example usage
database = database_provider.retrieve_database("your_database_id")
page = page_provider.retrieve_page("your_page_id")
```

## Documentation

[Doxygen Documentation](https://real1tyy.github.io/notion-apilib-python/) \
[Usage Examples](docs/examples) \
[Changelog](docs/CHANGELOG.md)

### Main Package Modules Breakdown

#### notion-apilib:

- Contains the core NotionApi class used for accessing the pages, database and blocks providers used for interacting
  with Notion API.

#### notion-apilib.data:

- Contains inside Pydantic models and factory methods for Notion objects like Page, Database, Block, Properties, etc.

#### notion-apilib.data.blocks:

- Pydantic models and factory methods for blocks.

#### notion-apilib.data.properties:

- Pydantic models and factory methods for page and database properties as well as Filter and Sort objects.

#### notion-apilib.data.structures:

- Pydantic models and factory methods for low-level structures like RichText and Annotations used by other objects.

### External:

1. [Notion API Documentation](https://developers.notion.com/reference/intro)
2. [Developers Notion](https://developers.notion.com/)
3. [Notion Integration](https://notionintegrations.com/)

## Contributing

This is my first library, and I know it might not be perfect. I welcome any suggestions, code reviews, documentation
improvements, bug reports or feature requests. Please feel free to contribute to the project.

### How to Contribute

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -am 'Add new feature').
4. Push the branch (git push origin feature-branch).
5. Open a Pull Request.

For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Feedback

As this is my first library, any constructive criticism or feedback is greatly appreciated. Whether it's a suggestion
for improvement or just a comment on how the library could be better, I'm eager to hear your thoughts. Please don't
hesitate to reach out if you have any ideas, feedback, or feature requests.
