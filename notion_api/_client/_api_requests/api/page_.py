# Standard Library
from dataclasses import dataclass
from typing import Optional

# Third Party
from requests import Response

# First Party
from notion_api.client._api_requests._utils.requests_ import RequestsClient


@dataclass
class NotionAPIPagesClient:
    requests_provider: RequestsClient

    def create_page(self, data: dict) -> Response:
        return self.requests_provider.perform_post_request("pages", data)

    def retrieve_page(
        self, page_id: str, query_params: Optional[str] = None
    ) -> Response:
        url = f"pages/{page_id}{query_params if query_params else ''}"
        return self.requests_provider.perform_get_request(url)

    def retrieve_page_property_item(
        self, page_id: str, property_id: str, query_params: Optional[str] = None
    ) -> Response:
        url = f"pages/{page_id}/properties/{property_id}{query_params if query_params else ''}"
        return self.requests_provider.perform_get_request(url)

    def update_page_properties(self, page_id: str, data: dict) -> Response:
        return self.requests_provider.perform_patch_request(f"pages/{page_id}", data)
