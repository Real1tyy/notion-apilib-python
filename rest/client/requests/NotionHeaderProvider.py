from dataclasses import dataclass

from client.requests.constants.notion import NOTION_VERSION
from client.requests.types import json_


@dataclass
class NotionHeaderProvider:
    api_key: str

    def create_header(self) -> json_:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json"
        }
