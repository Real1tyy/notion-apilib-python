# Standard Library
from dataclasses import dataclass

# Third Party
from notion_api.client._api_requests.constants.notion import NOTION_VERSION


@dataclass
class NotionHeaderProvider:
    api_key: str

    def create_header(self) -> dict:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json"
        }
