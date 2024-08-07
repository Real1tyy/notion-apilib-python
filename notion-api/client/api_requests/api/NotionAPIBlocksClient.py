# Standard Library
from dataclasses import dataclass
from typing import Optional

# Third Party
from client.api_requests.utils.RequestsClient import RequestsClient
from custom_types import json_
from requests import Response


@dataclass
class NotionAPIBlocksClient:
    requests_provider: RequestsClient

    def append_block_children(self, block_id: str, data: json_) -> Response:
        return self.requests_provider.perform_patch_request(f"blocks/{block_id}/children", data)

    def retrieve_block(self, block_id: str) -> Response:
        return self.requests_provider.perform_get_request(f"blocks/{block_id}")

    def retrieve_block_children(self, block_id: str, query_params: Optional[str] = None) -> Response:
        url = f"blocks/{block_id}/children{query_params if query_params else ''}"
        return self.requests_provider.perform_get_request(url)

    def update_block(self, block_id: str, data: json_) -> Response:
        return self.requests_provider.perform_patch_request(f"blocks/{block_id}", data)

    def delete_block(self, block_id: str) -> Response:
        return self.requests_provider.perform_delete_request(f"blocks/{block_id}")