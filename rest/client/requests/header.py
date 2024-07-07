from client.requests.types import json_

NOTION_VERSION = "2022-06-28"


def create_header(api_key) -> json_:
    return {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json"
    }
