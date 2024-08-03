from dataclasses import dataclass
from typing import Optional

from returns.result import Result, Success, Failure

from Block import Block
from CustomError import CustomError
from NotionBlockProvider import NotionBlockProvider
from Page import Page, create_page
from client.api_requests.api.NotionAPIPagesClient import NotionAPIPagesClient
from custom_types import json_
from status_codes import SUCCESS, ERROR


@dataclass
class NotionPageProvider:
    notion_client: NotionAPIPagesClient
    block_provider: NotionBlockProvider

    def create_page(self, page: Page) -> Result[CustomError, Page]:
        data = page.model_dump(mode='json', exclude_none=True, exclude={'id', 'archived', 'in_trash'})
        result = self.notion_client.create_page(data)
        if result.status_code != SUCCESS:
            return Failure(CustomError(message=result.text, status_code=result.status_code))
        try:
            page = create_page(result.json())
            return self.get_page_children(page)
        except Exception as e:
            return Failure(CustomError(message=str(e), status_code=ERROR))

    def retrieve_page(self, page_id: str, query_params: Optional[str] = None) -> Result[CustomError, Page]:
        response = self.notion_client.retrieve_page(page_id, query_params)
        if response.status_code != SUCCESS:
            return Failure(CustomError(response.status_code, response.text))

        try:
            return Success(create_page(response.json()))
        except Exception as e:
            return Failure(CustomError(message=str(e), status_code=ERROR))

    def retrieve_page_property_item(self, page_id: str, property_id: str, query_params: Optional[str] = None) \
            -> Result[CustomError, json_]:
        response = self.notion_client.retrieve_page_property_item(page_id, property_id, query_params)
        return Success(response.json()) if response.status_code == SUCCESS else Failure(
            CustomError(response.status_code, response.text))

    def update_page(self, page: Page) -> Result[CustomError, Page]:
        data = page.deserialize_json()
        response = self.notion_client.update_page_properties(page.id.hex, data)
        if response.status_code != SUCCESS:
            return Failure(CustomError(response.status_code, response.text))
        try:
            return Success(create_page(response.json()))
        except Exception as e:
            return Failure(CustomError(message=str(e), status_code=ERROR))

    def get_page_children(self, page: Page) -> Result[CustomError, Page]:
        children = self.block_provider.retrieve_children(page.id)
        if isinstance(children, Failure):
            return Failure(children.failure())
        page.children = children.unwrap()
        return Success(page)

    def delete_page(self, page: Page) -> Result[CustomError, bool]:
        page.in_trash = True
        result = self.update_page(page)
        return Success(True) if isinstance(Success, result) else Failure(result.failure())

    def set_page_children(self, page: Page) -> Result[CustomError, list[Block]]:
        page = self.retrieve_page(page.id.hex)
        if isinstance(page, Failure):
            return Failure(page.failure())
        page = page.unwrap()

        for child in page.children:
            result = self.block_provider.delete_block(child)
            if isinstance(result, Failure):
                return Failure(result.failure())

        return self.block_provider.append_block_children(page.hex.id, page.children)
