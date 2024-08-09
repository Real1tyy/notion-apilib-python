# Third Party
from client._api_requests.api.NotionAPIBlocksClient import NotionAPIBlocksClient
from client._api_requests.api.NotionAPIDatabasesClient import NotionAPIDatabasesClient
from client._api_requests.api.NotionAPIPagesClient import NotionAPIPagesClient
from client._api_requests._utils.NotionHeaderProvider import NotionHeaderProvider
from client._api_requests._utils.RequestsClient import RequestsClient
from client.block import NotionBlockProvider
from client.database import NotionDatabaseProvider
from client.page import NotionPageProvider
from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    _header_provider: NotionHeaderProvider = providers.Singleton(
        NotionHeaderProvider,
        config.api_key
    )

    _requests_client: RequestsClient = providers.Singleton(
        RequestsClient,
        header=providers.Callable(
            lambda notion_header_provider: notion_header_provider.create_header(),
            _header_provider)
    )

    _notion_api_blocks_client: NotionAPIBlocksClient = providers.Singleton(
        NotionAPIBlocksClient,
        requests_provider=_requests_client
    )

    _notion_api_pages_client: NotionAPIPagesClient = providers.Singleton(
        NotionAPIPagesClient,
        requests_provider=_requests_client,
    )

    _notion_api_databases_client: NotionAPIDatabasesClient = providers.Singleton(
        NotionAPIDatabasesClient,
        requests_provider=_requests_client
    )

    _notion_block_provider: NotionBlockProvider = providers.Singleton(
        NotionBlockProvider,
        notion_client=_notion_api_blocks_client
    )

    _notion_page_provider: NotionPageProvider = providers.Singleton(
        NotionPageProvider,
        notion_client=_notion_api_pages_client,
        block_provider=_notion_block_provider
    )

    _notion_database_provider: NotionDatabaseProvider = providers.Singleton(
        NotionDatabaseProvider,
        notion_client=_notion_api_databases_client
    )


class NotionApi:
    def __init__(self, api_key: str):
        self.container = Container()
        self.container.config.api_key.from_value(api_key)
        self.container.init_resources()

    def get_page_provider(self):
        return self.container._notion_page_provider()

    def get_block_provider(self):
        return self.container._notion_block_provider()

    def get_database_provider(self):
        return self.container._notion_database_provider()


__all__ = ["NotionApi"]
