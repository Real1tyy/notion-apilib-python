import json
from dataclasses import dataclass
from typing import Optional

from requests import Response
from returns.result import Result, Success, Failure

from CustomError import CustomError
from Page import Page
from client.api_requests.api.NotionAPIPagesClient import NotionAPIPagesClient
from custom_types import json_
from status_codes import SUCCESS


@dataclass
class NotionPageProvider:
    notion_client: NotionAPIPagesClient

    def create_page(self, page: Page) -> Result[CustomError, bool]:
        data = page.model_dump(mode='json', exclude_none=True, exclude={'id', 'archived', 'in_trash'})
        result = self.notion_client.create_page(data)
        return Success(True) if result.status_code == 200 \
            else Failure(CustomError(message=result.text, status_code=result.status_code))

    def retrieve_page(self, page_id: str, query_params: Optional[str] = None) -> Response:
        response = self.notion_client.retrieve_page(page_id, query_params)
        if response.status_code != SUCCESS:
            return Failure(CustomError(response.status_code, response.text))

        print(json.dumps(response.json(), indent=4))

        page = Page(**response.json())
        return Success(page)

    def retrieve_page_property_item(self, page_id: str, property_id: str, query_params: Optional[str] = None) \
            -> Response:
        return self.notion_client.retrieve_page_property_item(page_id, property_id, query_params)

    def update_page_properties(self, page_id: str, data: json_) -> Response:
        return self.notion_client.update_page_properties(page_id, data)
