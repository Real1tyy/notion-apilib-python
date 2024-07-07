import time
from typing import Optional

import requests
from requests import Response

from client.NotionHeaderProvider import NotionHeaderProvider


class RequestsProvider:
    BASE_URL = "https://api.notion.com/v1/"

    def __init__(self, notion_header_provider: NotionHeaderProvider):
        self.header = notion_header_provider.create_header()

    @staticmethod
    def check_response_status(response: Response) -> bool:
        if response.status_code == 200:
            return True
        if response.status_code == 429:
            print("Timed out rate limit reached")
            time.sleep(1)
        return False

    def perform_request(self, url: str) -> Optional[dict[str, str]]:
        final_url = self.BASE_URL + url
        response = requests.get(final_url, headers=self.header)
        return response.json() if self.check_response_status(response) else None
