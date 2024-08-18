# Standard Library
from dataclasses import dataclass
from typing import Optional

# Third Party
from requests import Response

from .._utils.requests_ import RequestsClient


@dataclass
class NotionAPIBlocksClient:
    requests_provider: RequestsClient

    def append_block_children(self, block_id: str, data: dict) -> Response:
        return self.requests_provider.perform_patch_request(f"blocks/{block_id}/children", data)

    def retrieve_block(self, block_id: str) -> Response:
        return self.requests_provider.perform_get_request(f"blocks/{block_id}")

    def retrieve_block_children(self, block_id: str, data: dict) -> Response:
        url = f"blocks/{block_id}/children"
        return self.requests_provider.perform_get_request(url, data)

    def update_block(self, block_id: str, data: dict) -> Response:
        return self.requests_provider.perform_patch_request(f"blocks/{block_id}", data)

    def delete_block(self, block_id: str) -> Response:
        return self.requests_provider.perform_delete_request(f"blocks/{block_id}")
