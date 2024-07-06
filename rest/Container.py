from dependency_injector import containers, providers

from client.NotionAPIClient import NotionAPIClient
from client.RequestsProvider import RequestsProvider


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    requests_provider = providers.Singleton(
        RequestsProvider,
        api_key=config.api_key
    )

    notion_api_client = providers.Singleton(
        NotionAPIClient,
        requests_provider=requests_provider
    )
