from dotenv import load_dotenv

from Container import Container

if __name__ == "__main__":
    load_dotenv()

    container = Container()
    container.config.api_key.from_env("NOTION_INTEGRATION_KEY")

    notion_database_provider = container.notion_database_provider()
    notion_page_provider = container.notion_page_provider()
    notion_client = container.notion_api_client()

    # page = notion_page_provider.get_page("c8e3505e2341488e9462542023f599cd")
    #
    # print(repr(page))

    response = notion_client.get_database("1a91e289d5d9470d9e30ff1dfde63c60")
    for key, value in response["properties"].items():
        print(key, value)

    response2 = notion_database_provider.get_database("1a91e289d5d9470d9e30ff1dfde63c60")
    # print(json.dumps(response2["properties"], indent=4))
