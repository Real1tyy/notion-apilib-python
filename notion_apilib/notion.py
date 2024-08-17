# Third Party
from dependency_injector import containers, providers

# First Party
from notion_apilib._client import NotionBlockProvider, NotionDatabaseProvider, NotionPageProvider
from notion_apilib._client._api_requests import (
    NotionAPIBlocksClient,
    NotionAPIDatabasesClient,
    NotionAPIPagesClient,
    NotionHeaderProvider,
    RequestsClient,
)


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    _header_provider: NotionHeaderProvider = providers.Singleton(
        NotionHeaderProvider, config.api_key
    )

    _requests_client: RequestsClient = providers.Singleton(
        RequestsClient,
        header=providers.Callable(
            lambda notion_header_provider: notion_header_provider.create_header(),
            _header_provider,
        ),
    )

    _notion_api_blocks_client: NotionAPIBlocksClient = providers.Singleton(
        NotionAPIBlocksClient, requests_provider=_requests_client
    )

    _notion_api_pages_client: NotionAPIPagesClient = providers.Singleton(
        NotionAPIPagesClient,
        requests_provider=_requests_client,
    )

    _notion_api_databases_client: NotionAPIDatabasesClient = providers.Singleton(
        NotionAPIDatabasesClient, requests_provider=_requests_client
    )

    _notion_block_provider: NotionBlockProvider = providers.Singleton(
        NotionBlockProvider, notion_client=_notion_api_blocks_client
    )

    _notion_page_provider: NotionPageProvider = providers.Singleton(
        NotionPageProvider,
        notion_client=_notion_api_pages_client,
        block_provider=_notion_block_provider,
    )

    _notion_database_provider: NotionDatabaseProvider = providers.Singleton(
        NotionDatabaseProvider, notion_client=_notion_api_databases_client
    )


class NotionApi:
    def __init__(self, api_key: str):
        self.container = Container()
        self.container.config.api_key.from_value(api_key)
        self.container.init_resources()

    @property
    def page_provider(self):
        return self.container._notion_page_provider()

    @property
    def block_provider(self):
        return self.container._notion_block_provider()

    @property
    def database_provider(self):
        return self.container._notion_database_provider()


__all__ = ["NotionApi"]
