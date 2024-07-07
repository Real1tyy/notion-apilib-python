from typing import Optional

from client.requests.RequestsProvider import RequestsProvider
from client.requests.types import json_


class NotionAPIClient:

    def __init__(self, requests_provider: RequestsProvider):
        self.requests_provider = requests_provider

    def append_block_children(self, block_id: str, data: json_) -> Optional[json_]:
        return self.requests_provider.perform_patch_request("blocks/" + block_id + "/children", data)

    def retrieve_block(self, block_id: str) -> Optional[json_]:
        return self.requests_provider.perform_get_request("blocks/" + block_id)

    def retrieve_block_children(self, block_id: str, query_params: Optional[str] = None) -> Optional[json_]:
        url = f"blocks/{block_id}/children{query_params if query_params else ''}"
        return self.requests_provider.perform_get_request(url)

    def update_block(self, block_id: str, data: json_) -> Optional[json_]:
        return self.requests_provider.perform_patch_request("blocks/" + block_id, data)

    def delete_block(self, block_id: str) -> Optional[json_]:
        return self.requests_provider.perform_delete_request("blocks/" + block_id)

    def create_page(self, data: json_) -> Optional[json_]:
        return self.requests_provider.perform_post_request("pages", data)

    def get_page(self, page_id: str) -> Optional[json_]:
        return self.requests_provider.perform_get_request("pages/" + page_id)

    def get_block(self, block_id: str) -> Optional[json_]:
        return self.requests_provider.perform_get_request("blocks/" + block_id)

    def get_database(self, database_id: str) -> Optional[json_]:
        return self.requests_provider.perform_get_request("databases/" + database_id)

    def query_database(self, database_id: str) -> Optional[json_]:
        return self.requests_provider.perform_post_request("databases/" + database_id + "/query")
