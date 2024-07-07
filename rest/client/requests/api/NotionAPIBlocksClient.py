from dataclasses import dataclass
from typing import Optional

from client.requests.RequestsProvider import RequestsProvider
from client.requests.types import json_


@dataclass
class NotionAPIBlocksClient:
    requests_provider: RequestsProvider

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
