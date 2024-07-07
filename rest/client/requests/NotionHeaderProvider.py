from dataclasses import dataclass

from client.requests.constants.notion import NOTION_VERSION
from client.requests.types import json_


@dataclass
class NotionHeaderProvider:

    def __init__(self, api_key: str):
        self.api_key = api_key

    def create_header(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Notion-Version": NotionHeaderProvider.NOTION_VERSION,
            "Content-Type": "application/json"
        }


def create_header(api_key) -> json_:
    print(type(api_key))
    return {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json"
    }
