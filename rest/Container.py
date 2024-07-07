from dependency_injector import containers, providers

from client.NotionBlockProvider import NotionBlockProvider
from client.NotionDatabaseProvider import NotionDatabaseProvider
from client.NotionPageProvider import NotionPageProvider
from client.requests.NotionHeaderProvider import NotionHeaderProvider
from client.requests.RequestsClient import RequestsClient
from client.requests.api.NotionAPIBlocksClient import NotionAPIBlocksClient
from client.requests.api.NotionAPIDatabasesClient import NotionAPIDatabasesClient
from client.requests.api.NotionAPIPagesClient import NotionAPIPagesClient


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    notion_header_provider = providers.Singleton(
        NotionHeaderProvider,
        config.api_key
    )

    requests_provider = providers.Singleton(
        RequestsClient,
        header=providers.Callable(
            lambda notion_header_provider: notion_header_provider.create_header(),
            notion_header_provider)
    )

    notion_api_blocks_client = providers.Singleton(
        NotionAPIBlocksClient,
        requests_provider=requests_provider
    )

    notion_api_pages_client = providers.Singleton(
        NotionAPIPagesClient,
        requests_provider=requests_provider
    )

    notion_api_databases_client = providers.Singleton(
        NotionAPIDatabasesClient,
        requests_provider=requests_provider
    )

    notion_block_provider = providers.Singleton(
        NotionBlockProvider,
        notion_api_blocks_client=notion_api_blocks_client
    )

    notion_page_provider = providers.Singleton(
        NotionPageProvider,
        notion_api_pages_client=notion_api_pages_client
    )

    notion_database_provider = providers.Singleton(
        NotionDatabaseProvider,
        notion_api_databases_client=notion_api_databases_client
    )
