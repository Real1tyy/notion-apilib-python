from typing import Optional

from client.RequestsProvider import RequestsProvider


class NotionClient:

    def __init__(self, requests_provider: RequestsProvider):
        self.requests_provider = requests_provider

    def get_page(self, page_id: str) -> Optional[dict[str, str]]:
        return self.requests_provider.perform_request("pages/" + page_id)

    def get_block(self, block_id: str) -> Optional[dict[str, str]]:
        return self.requests_provider.perform_request("blocks/" + block_id)

    def get_database(self, database_id: str) -> Optional[dict[str, str]]:
        return self.requests_provider.perform_request("databases/" + database_id)
