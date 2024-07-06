class NotionHeaderProvider:
    NOTION_VERSION = "2022-06-28"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def create_header(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Notion-Version": NotionHeaderProvider.NOTION_VERSION,
            "Content-Type": "application/json"
        }
