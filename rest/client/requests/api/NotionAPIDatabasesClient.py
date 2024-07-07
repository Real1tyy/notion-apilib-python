from dataclasses import dataclass
from typing import Optional

from client.requests.RequestsProvider import RequestsProvider
from client.requests.types import json_


@dataclass
class NotionAPIDatabasesClient:
    requests_provider: RequestsProvider

    def create_database(self, data: json_) -> Optional[json_]:
        return self.requests_provider.perform_post_request("databases", data)

    def query_database(self, database_id: str, query_params: str, data: json_) -> Optional[json_]:
        url = f"databases/{database_id}/query{query_params if query_params else ''}"
        return self.requests_provider.perform_post_request(url, data)

    def retrieve_database(self, database_id: str) -> Optional[json_]:
        return self.requests_provider.perform_get_request(f"databases/{database_id}")

    def update_database(self, database_id: str, data: json_) -> Optional[json_]:
        return self.requests_provider.perform_patch_request(f"databases/{database_id}", data)
