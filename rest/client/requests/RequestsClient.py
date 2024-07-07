from dataclasses import dataclass
from typing import Optional, Callable

import requests

from client.requests.constants.notion import BASE_URL
from client.requests.types import json_


@dataclass
class RequestsProvider:
    header: str

    def perform_get_request(self, url: str) -> Optional[json_]:
        return self.perform_request(url, requests.get)

    def perform_post_request(self, url: str, data: Optional[json_] = None) -> Optional[json_]:
        return self.perform_request(url, requests.post, data)

    def perform_put_request(self, url: str, data: Optional[json_] = None) -> Optional[json_]:
        return self.perform_request(url, requests.put, data)

    def perform_patch_request(self, url: str, data: Optional[json_] = None) -> Optional[json_]:
        return self.perform_request(url, requests.patch, data)

    def perform_delete_request(self, url: str) -> Optional[json_]:
        return self.perform_request(url, requests.delete)

    def perform_request(self, url: str, method: Callable[..., requests.Response], data: Optional[json_] = None) -> (
            Optional)[json_]:
        final_url = BASE_URL + url
        response = method(final_url, headers=self.header, json=data)
        return response.json()
