from dependency_injector import containers, providers

from client.NotionAPIClient import NotionAPIClient
from client.NotionBlockProvider import NotionBlockProvider
from client.NotionDatabaseProvider import NotionDatabaseProvider
from client.NotionHeaderProvider import NotionHeaderProvider
from client.NotionPageProvider import NotionPageProvider
from client.RequestsProvider import RequestsProvider


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    notion_header_provider = providers.Singleton(
        NotionHeaderProvider,
        api_key=config.api_key
    )

    requests_provider = providers.Singleton(
        RequestsProvider,
        notion_header_provider=notion_header_provider
    )

    notion_api_client = providers.Singleton(
        NotionAPIClient,
        requests_provider=requests_provider
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
