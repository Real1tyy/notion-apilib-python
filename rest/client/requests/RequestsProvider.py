import time
from dataclasses import dataclass
from typing import Optional, Callable

import requests
from requests import Response

from client.requests.types import json_


@dataclass
class RequestsProvider:
    BASE_URL = "https://api.notion.com/v1/"
    header: str

    @staticmethod
    def check_response_status(response: Response) -> bool:
        if response.status_code == 200:
            return True
        if response.status_code == 429:
            print("Timed out rate limit reached")
            time.sleep(1)
        return False

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
        final_url = self.BASE_URL + url
        response = method(final_url, headers=self.header, json=data)
        return response.json() if self.check_response_status(response) else None
