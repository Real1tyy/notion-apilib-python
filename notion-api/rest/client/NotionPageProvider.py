from dataclasses import dataclass
from typing import Optional

from returns.result import Result, Success, Failure

from CustomError import CustomError
from Page import Page, create_page
from client.api_requests.api.NotionAPIPagesClient import NotionAPIPagesClient
from custom_types import json_
from status_codes import SUCCESS, ERROR


@dataclass
class NotionPageProvider:
    notion_client: NotionAPIPagesClient

    def create_page(self, page: Page) -> Result[CustomError, Page]:
        data = page.model_dump(mode='json', exclude_none=True, exclude={'id', 'archived', 'in_trash'})
        result = self.notion_client.create_page(data)
        if result.status_code != SUCCESS:
            return Failure(CustomError(message=result.text, status_code=result.status_code))
        try:
            return Success(create_page(result.json()))
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
