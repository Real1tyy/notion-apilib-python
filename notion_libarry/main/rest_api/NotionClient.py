from typing import Optional

import requests
from requests import Response


class NotionClient:
    BASE_URL = "https://api.notion.com/v1/"
    NOTION_VERSION = "2022-06-28"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.header = self.create_header()

    def create_header(self) -> dict[str, str]:
        return {
                "Authorization": f"Bearer {self.api_key}",
                "Notion-Version": self.NOTION_VERSION,
                "Content-Type": "application/json"
        }

    def __check_connection(self, response: Response) -> bool:
        if response.status_code == 200:
            return True
        else:
            return False

    def get_page(self, page_id: str) -> Optional[Response]:
        PAGES_URL = self.BASE_URL + "pages/"
        final_url = PAGES_URL + page_id
        response = requests.get(final_url, headers=self.header)

        if self.__check_connection(response):
            return response

        return None

    # def get_database(self, database_id: str):
