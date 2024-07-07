from client.requests.types import json_


class NotionHeaderProvider:
    NOTION_VERSION = "2022-06-28"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def create_header(self) -> json_:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Notion-Version": NotionHeaderProvider.NOTION_VERSION,
            "Content-Type": "application/json"
        }
