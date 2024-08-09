# Standard Library
from dataclasses import dataclass

# Third Party
from client._api_requests.constants.notion import NOTION_VERSION
from custom_types import json_


@dataclass
class NotionHeaderProvider:
    api_key: str

    def create_header(self) -> json_:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json"
        }
