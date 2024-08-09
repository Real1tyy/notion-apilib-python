# Standard Library
from dataclasses import dataclass
from typing import Optional, Any

from requests import Response

# Third Party
from client._api_requests.api.NotionAPIDatabasesClient import NotionAPIDatabasesClient
from data import Database, deserialize_database
from page import deserialize_page
from sort import Sort
from utils import _get_children_from_json, _handle_pagination, _prepare_query_data


@dataclass
class NotionDatabaseProvider:
    """
        Provides API methods to interact with Notion API database endpoints using and returning DSL database objects.
    """
    notion_client: NotionAPIDatabasesClient

    def create_database(self, database: Database) -> Database:
        """
        Creates a new database in Notion.

        Args:
            database (Database): The database object to create.

        Returns:
            Database: The created database with its details filled in from the Notion API.

        Raises:
            ValueError: If the deserialization of the response fails due to an invalid schema.
            ResponseException: If the Notion API returns an error status code.
        """
        response = self.notion_client.create_database(database.serialize_to_json())
        return deserialize_database(response.json())

    def query_database(
            self, database: Database, filter: Optional[str] = None, sort: Optional[list[Sort]] =
            None) -> (
            Database):
        """
        Queries a Notion database and retrieves its pages based on optional filters and sorting.

        Args:
            database (Database): The database object to query.
            filter (Optional[str]): Optional filter string for the query.
            sort (Optional[str]): Optional sorting criteria for the query.

        Returns:
            Database: The database object with its pages filled in from the query results.

        Raises:
            ValueError: If the deserialization of the response fails due to an invalid schema.
            ResponseException: If the Notion API returns an error status code.
        """
        database.pages = []
        data = _prepare_query_data(sort=sort, filter=filter)
        response = self.notion_client.query_database(database.id.hex, data)
        children = _get_children_from_json(response)
        database.pages.extend(map(deserialize_page, children))
        return _handle_pagination(
            database, response, self._query_paginated_database,
            filter=filter, sort=sort)

    def _query_paginated_database(
            self, database: Database, next_cursor: str, filter: Optional[str] = None,
            sort: dict[str, Any] = None) -> Database:
        """
        Handles paginated queries to a Notion database.

        Args:
            database (Database): The database object to query.
            next_cursor (str): The cursor to start the next page of results.
            filter (Optional[str]): Optional filter string for the query.
            sort (Optional[str]): Optional sorting criteria for the query.

        Returns:
            Database: The database object with its pages filled in from the paginated query results.

        Raises:
            ValueError: If the deserialization of the response fails due to an invalid schema.
            ResponseException: If the Notion API returns an error status code.
        """
        data = _prepare_query_data(next_cursor, sort, filter)
        response = self.notion_client.query_database(database.id.hex, data, None)
        children = _get_children_from_json(response)

        for page_json in children:
            try:
                page = deserialize_page(page_json)
            except Exception as e:
                print(page_json['_properties'])
                raise e
            database.pages.append(page)

        return _handle_pagination(
            database, response, self._query_paginated_database,
            filter=filter, sort=sort)

    def retrieve_database(self, database_id: str) -> Database:
        """
        Retrieves the details of a specific Notion database by its ID.

        Args:
            database_id (str): The ID of the database to retrieve.

        Returns:
            Database: The retrieved database object.

        Raises:
            ValueError: If the deserialization of the response fails due to an invalid schema.
            ResponseException: If the Notion API returns an error status code.
        """
        response = self.notion_client.retrieve_database(database_id)
        return deserialize_database(response.json())

    def update_database(self, database: Database) -> Database:
        """
        Updates an existing Notion database with new data.

        Args:
            database (Database): The database object with updated data.

        Returns:
            Database: The updated database object as returned by the Notion API.

        Raises:
            ValueError: If the deserialization of the response fails due to an invalid schema.
            ResponseException: If the Notion API returns an error status code.
        """
        data = database.serialize_to_json()
        response = self.notion_client.update_database(database.id.hex, data)
        return deserialize_database(response.json())

# how to retrieve the latest results from a Notion database
# {
#  "timestamp": "last_edited_time",
#  "direction": "descending"
# }
