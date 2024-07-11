from dataclasses import dataclass
from typing import Optional

from requests import Response

from client.api_requests.custom_types import json_
from client.api_requests.utils.RequestsClient import RequestsClient


@dataclass
class NotionAPIDatabasesClient:
    requests_provider: RequestsClient

    def create_database(self, data: json_) -> Response:
        return self.requests_provider.perform_post_request("databases", data)

    def query_database(self, database_id: str, data: json_, query_params: Optional[str] = None) -> Response:
        url = f"databases/{database_id}/query{query_params if query_params else ''}"
        return self.requests_provider.perform_post_request(url, data)

    def retrieve_database(self, database_id: str) -> Response:
        return self.requests_provider.perform_get_request(f"databases/{database_id}")

    def update_database(self, database_id: str, data: json_) -> Response:
        return self.requests_provider.perform_patch_request(f"databases/{database_id}", data)
