from dataclasses import dataclass
from typing import Optional

from requests import Response

from client.requests.api.NotionAPIPagesClient import NotionAPIPagesClient
from client.requests.types import json_


@dataclass
class NotionPageProvider:
    notion_client: NotionAPIPagesClient

    def create_page(self, data: json_) -> Response:
        return self.notion_client.create_page(data)

    def retrieve_page(self, page_id: str, query_params: Optional[str] = None) -> Response:
        return self.notion_client.retrieve_page(page_id, query_params)

    def retrieve_page_property_item(self, page_id: str, property_id: str, query_params: Optional[str] = None) \
            -> Response:
        return self.notion_client.retrieve_page_property_item(page_id, property_id, query_params)

    def update_page_properties(self, page_id: str, data: json_) -> Response:
        return self.notion_client.update_page_properties(page_id, data)

# how to retrieve the latest results from a Notion database
# {
#  "timestamp": "last_edited_time",
#  "direction": "descending"
# }
