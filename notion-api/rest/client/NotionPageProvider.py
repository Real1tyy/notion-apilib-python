# Standard Library
from dataclasses import dataclass
from typing import Optional

from returns.result import Failure, Result, Success

# Third Party
from ApiError import ApiError
from NotionBlockProvider import NotionBlockProvider
from _blocks import Block
from client.api_requests.api.NotionAPIPagesClient import NotionAPIPagesClient
from custom_types import json_
from decorators import handle_exceptions
from page import Page, create_page
from status_codes import SUCCESS


@dataclass
class NotionPageProvider:
    notion_client: NotionAPIPagesClient
    block_provider: NotionBlockProvider

    @handle_exceptions
    def create_page(self, page: Page) -> Result[ApiError, Page]:
        data = page.model_dump(mode='json', exclude_none=True, exclude={'id', 'archived', 'in_trash'})
        result = self.notion_client.create_page(data)
        if result.status_code != SUCCESS:
            return Failure(ApiError(message=result.text, status_code=result.status_code))

        page = create_page(result.json())
        return self.get_page_children(page)

    @handle_exceptions
    def retrieve_page(self, page_id: str, query_params: Optional[str] = None) -> Result[ApiError, Page]:
        response = self.notion_client.retrieve_page(page_id, query_params)
        if response.status_code != SUCCESS:
            return Failure(ApiError(response.status_code, response.text))

        return create_page(response.json())

    @handle_exceptions
    def retrieve_page_property_item(self, page_id: str, property_id: str, query_params: Optional[str] = None) \
            -> Result[ApiError, json_]:
        response = self.notion_client.retrieve_page_property_item(page_id, property_id, query_params)
        return response.json() if response.status_code == SUCCESS else Failure(
            ApiError(response.status_code, response.text))

    @handle_exceptions
    def update_page(self, page: Page) -> Result[ApiError, Page]:
        data = page.deserialize_json()
        response = self.notion_client.update_page_properties(page.id.hex, data)
        if response.status_code != SUCCESS:
            return Failure(ApiError(response.status_code, response.text))
        return create_page(response.json())

    @handle_exceptions
    def get_page_children(self, page: Page) -> Result[ApiError, Page]:
        children = self.block_provider.retrieve_children(page.id)
        if isinstance(children, Failure):
            return Failure(children.failure())
        page.children = children.unwrap()
        return page

    @handle_exceptions
    def delete_page(self, page: Page) -> Result[ApiError, bool]:
        page.in_trash = True
        result = self.update_page(page)
        return True if isinstance(Success, result) else Failure(result.failure())

    @handle_exceptions
    def set_page_children(self, page: Page) -> Result[ApiError, list[Block]]:
        page = self.retrieve_page(page.id.hex)
        if isinstance(page, Failure):
            return Failure(page.failure())
        page = page.unwrap()

        for child in page.children:
            result = self.block_provider.delete_block(child)
            if isinstance(result, Failure):
                return Failure(result.failure())

        return self.block_provider.append_block_children(page.hex.id, page.children)
