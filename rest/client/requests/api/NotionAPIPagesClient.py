from dataclasses import dataclass
from typing import Optional

from client.requests.RequestsProvider import RequestsProvider
from client.requests.types import json_


@dataclass
class NotionAPIPagesClient:
    requests_provider: RequestsProvider

    def create_page(self, data: json_) -> Optional[json_]:
        return self.requests_provider.perform_post_request("pages", data)

    def retrieve_page(self, page_id: str, query_params: str) -> Optional[json_]:
        url = f"pages/{page_id}{query_params if query_params else ''}"
        return self.requests_provider.perform_get_request(url)

    def retrieve_page_property_item(self, page_id: str, property_id: str, query_params: str) -> Optional[json_]:
        url = f"pages/{page_id}/properties/{property_id}{query_params if query_params else ''}"
        return self.requests_provider.perform_get_request(url)

    def update_page_properties(self, page_id: str, data: json_) -> Optional[json_]:
        return self.requests_provider.perform_patch_request(f"pages/{page_id}", data)
