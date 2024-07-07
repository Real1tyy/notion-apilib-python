from dependency_injector import containers, providers

from client.NotionBlockProvider import NotionBlockProvider
from client.NotionDatabaseProvider import NotionDatabaseProvider
from client.NotionPageProvider import NotionPageProvider
from client.requests.RequestsProvider import RequestsProvider
from client.requests.api.NotionAPIBlocksClient import NotionAPIBlocksClient
from client.requests.api.NotionAPIClient import NotionAPIClient
from client.requests.api.NotionAPIDatabasesClient import NotionAPIDatabasesClient
from client.requests.api.NotionAPIPagesClient import NotionAPIPagesClient
from client.requests.header import create_header


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    requests_provider = providers.Singleton(
        RequestsProvider,
        header=create_header(config.api_key)
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

    notion_api_client = providers.Singleton(
        NotionAPIClient,
        notion_api_databases_client=notion_api_databases_client,
        notion_api_pages_client=notion_api_pages_client,
        notion_api_blocks_client=notion_api_blocks_client
    )

    notion_block_provider = providers.Singleton(
        NotionBlockProvider,
        notion_api_client=notion_api_client
    )

    notion_page_provider = providers.Singleton(
        NotionPageProvider,
        notion_api_client=notion_api_client
    )

    notion_database_provider = providers.Singleton(
        NotionDatabaseProvider,
        notion_api_client=notion_api_client
    )
