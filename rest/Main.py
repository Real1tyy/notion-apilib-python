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

    response = notion_client.query_database("1a91e289d5d9470d9e30ff1dfde63c60")
    print(len(response["results"]))
    for val in response["results"]:
        if val["id"] == "faee723c-002f-445e-ad3a-d943dbcd5811":
            print(val)

    response2 = notion_client.notion_pages_client.retrieve_page("faee723c-002f-445e-ad3a-d943dbcd5811")
    print(response2)
    # for value in response["properties"].values():
    #     print(value)

    # response2 = notion_database_provider.get_database("1a91e289d5d9470d9e30ff1dfde63c60")
    # # print(response2)
    # for val in response2.properties:
    #     print(val)
