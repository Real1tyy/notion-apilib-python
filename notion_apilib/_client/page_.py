# Standard Library
from dataclasses import dataclass
from typing import Any, Optional

# First Party
from ._api_requests import NotionAPIPagesClient
from .block_ import NotionBlockProvider
from notion_apilib.data import Page, deserialize_page


@dataclass
class NotionPageProvider:
    """
    Provides API methods to interact with Notion API pages endpoints using and returning DSL pages objects.
    """

    notion_client: NotionAPIPagesClient
    block_provider: NotionBlockProvider

    def create_page(self, page: Page) -> Page:
        """
        Creates a page in the Notion API with the values of the passed Page object.
        The 'id', 'archived', and 'in_trash' attributes will be excluded as they are not needed during creation.

        Parameters:
            page (Page): The Page object to create.

        Returns:
            Page: The created Page object with data returned from the Notion API.

        Raises:
            ValueError: If the deserialization of the response fails due to an invalid schema.
            ResponseException: If the Notion API returns an error status code.
        """
        data = page.model_dump(
            mode="json", exclude_none=True, exclude={"id", "archived", "in_trash"}
        )
        result = self.notion_client.create_page(data)
        return deserialize_page(result.json())

    def retrieve_page(self, page_id: str, query_params: Optional[str] = None) -> Page:
        """
        Retrieves a page from the Notion API by its ID and optionally retrieves the page's children.

        Parameters:
            page_id (str): The ID of the page to retrieve.
            query_params (Optional[str]): Optional query parameters to include in the request.

        Returns:
            Page: The retrieved Page object, including its children if they exist.

        Raises:
            ValueError: If the deserialization of the response fails due to an invalid schema.
            ResponseException: If the Notion API returns an error status code.
        """
        response = self.notion_client.retrieve_page(page_id, query_params)
        page = deserialize_page(response.json())
        return self.get_page_children(page)

    def retrieve_page_property_item(
            self, page_id: str, property_id: str, query_params: Optional[str] = None
    ) -> dict[str, Any]:
        """
        Retrieves a specific property item from a page in the Notion API.

        Parameters:
            page_id (str): The ID of the page containing the property.
            property_id (str): The ID of the property to retrieve.
            query_params (Optional[str]): Optional query parameters to include in the request.

        Returns:
            dict[str, Any]: The property item data as a dictionary.

        Raises:
            ResponseException: If the Notion API returns an error status code.
        """
        return self.notion_client.retrieve_page_property_item(
            page_id, property_id, query_params
        ).json()

    def update_page(self, page: Page) -> Page:
        """
        Updates a page in the Notion API with the values of the passed Page object.

        Parameters:
            page (Page): The Page object containing the updated data.

        Returns:
            Page: The updated Page object as returned by the Notion API.

        Raises:
            ValueError: If the deserialization of the response fails due to an invalid schema.
            ResponseException: If the Notion API returns an error status code.
        """
        data = page.serialize_to_json()
        response = self.notion_client.update_page_properties(page.id.hex, data)
        return deserialize_page(response.json())

    def get_page_children(self, page: Page) -> Page:
        """
        Retrieves and appends the children blocks of a given page.

        Parameters:
            page (Page): The Page object whose children blocks are to be retrieved.

        Returns:
            Page: The Page object with its children blocks populated.

        Raises:
            ValueError: If the deserialization of the response fails due to an invalid schema.
            ResponseException: If the Notion API returns an error status code.
        """
        children = self.block_provider._retrieve_children(page.id)
        page.children = children
        return page

    def delete_page(self, page: Page) -> None:
        """
        Moves a page to the trash in the Notion API by setting its 'in_trash' attribute to True.

        Parameters:
            page (Page): The Page object to be moved to the trash.

        Raises:
            ValueError: If the deserialization of the response fails due to an invalid schema.
            ResponseException: If the Notion API returns an error status code.
        """
        page.in_trash = True
        self.update_page(page)

    def set_page_children(self, page: Page) -> Page:
        """
        Sets the children blocks of a page in the Notion API. The current children will be deleted and replaced with the new ones.

        Parameters:
            page (Page): The Page object whose children blocks are to be set.

        Returns:
            Page: The updated Page object with its new children blocks.

        Raises:
            ValueError: If the deserialization of the response fails due to an invalid schema.
            ResponseException: If the Notion API returns an error status code.
        """
        page = self.retrieve_page(page.id.hex)
        [self.block_provider.delete_block(child) for child in page.children]
        page.children = self.block_provider.append_block_children(
            page.id.hex, page.children
        )
        return page
