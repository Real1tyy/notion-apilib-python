# Standard Library
import time
from dataclasses import dataclass
from typing import Callable, Optional

# Third Party
import requests

from client.exceptions import ResponseError
from client._api_requests.constants.notion import BASE_URL
from custom_types import json_
from requests import Response

from status_codes import SUCCESS, RATE_LIMIT


def verify_response(
        response: Response, perform_request: Callable[..., Response], url: str, method: Callable[...,
        Response], data: Optional[dict] = None) -> requests.Response:
    if response.status_code == RATE_LIMIT:
        time.sleep(0.2)
        return perform_request(url, method, data)

    if response.status_code != SUCCESS:
        raise ResponseError(response.status_code, response.text)

    return response


@dataclass
class RequestsClient:
    header: str

    def perform_get_request(self, url: str, data: Optional[json_] = None) -> Response:
        return self.perform_request(url, requests.get, data)

    def perform_post_request(self, url: str, data: Optional[json_] = None) -> Response:
        return self.perform_request(url, requests.post, data)

    def perform_put_request(self, url: str, data: Optional[json_] = None) -> Response:
        return self.perform_request(url, requests.put, data)

    def perform_patch_request(self, url: str, data: Optional[json_] = None) -> Response:
        return self.perform_request(url, requests.patch, data)

    def perform_delete_request(self, url: str) -> Response:
        return self.perform_request(url, requests.delete)

    def perform_request(self, url: str, method: Callable[..., Response], data: Optional[json_] = None) \
            -> Response:
        final_url = BASE_URL + url
        response = method(final_url, headers=self.header, json=data)
        return verify_response(response, self.perform_request, url, method, data)
