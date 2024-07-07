from dataclasses import dataclass

from client.requests.api.NotionAPIBlocksClient import NotionAPIBlocksClient
from client.requests.api.NotionAPIDatabasesClient import NotionAPIDatabasesClient
from client.requests.api.NotionAPIPagesClient import NotionAPIPagesClient


@dataclass
class NotionAPIClient:
    notion_blocks_client: NotionAPIBlocksClient
    notion_pages_client: NotionAPIPagesClient
    notion_databases_client: NotionAPIDatabasesClient
