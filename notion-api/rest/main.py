from dotenv import load_dotenv

from Container import Container

if __name__ == "__main__":
    load_dotenv()
    container: Container = Container()
    container.config.api_key.from_env("NOTION_INTEGRATION_KEY")

    database_provider = container.notion_database_provider()
    blocks_provider = container.notion_block_provider()
    page_provider = container.notion_page_provider()

    file_path = "links"
    with open(file_path, "r") as file:
        lines = file.readlines()
    for line in lines:
        if line != lines[4]:
            continue
        result = database_provider.retrieve_database(line.strip())
        database = result.unwrap()

    # response = notion_client.query_database("1a91e289d5d9470d9e30ff1dfde63c60")
    # print(len(response["results"]))
    # for val in response["results"]:
    #     if val["id"] == "faee723c-002f-445e-ad3a-d943dbcd5811":
    #         print(val)
    #
    # response2 = notion_client.notion_pages_client.retrieve_page("faee723c-002f-445e-ad3a-d943dbcd5811")
    # print(response2)
    # for value in response["properties"].values():
    #     print(value)
    #
    # response2 = notion_database_provider.get_database("1a91e289d5d9470d9e30ff1dfde63c60")
    # # print(response2)
    # for val in response2.properties:
    #     print(val)
