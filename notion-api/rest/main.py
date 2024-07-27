from dotenv import load_dotenv
from returns.result import Success

from Container import Container

if __name__ == "__main__":
    load_dotenv()
    container: Container = Container()
    container.config.api_key.from_env("NOTION_INTEGRATION_KEY")

    database_provider = container.notion_database_provider()
    blocks_provider = container.notion_block_provider()

    file_path = "links"
    with open(file_path, "r") as file:
        lines = file.readlines()

    # result = blocks_provider.retrieve_block("4b81ffd2ec3a4132a5835385f3b560de")
    # if isinstance(result, Success):
    #     result = result.unwrap()
    #     print(result)
    result2 = blocks_provider.retrieve_block("a0a0b919e15646ba833809c1dd555c6e")
    if isinstance(result2, Success):
        result = result2.unwrap()
        print(result2)
    # result2 = blocks_provider.retrieve_block_children("8c22d4e710dc4b68b52cdc39f92f2355")
    # print(result2)

    # for line in lines:
    #     if line != lines[4]:
    #         continue
    #     result = database_provider.retrieve_database(line.strip())
    #     if isinstance(result, Success):
    #         x = result.unwrap()
    #         print(type(x))
    #         print(x)
    #     if isinstance(result, Failure):
    #         print(result.unwrap())
    #
    # # page = notion_page_provider.get_page("c8e3505e2341488e9462542023f599cd")
    # #
    # # print(repr(page))
    #
    # # response = notion_client.query_database("1a91e289d5d9470d9e30ff1dfde63c60")
    # # print(len(response["results"]))
    # # for val in response["results"]:
    # #     if val["id"] == "faee723c-002f-445e-ad3a-d943dbcd5811":
    # #         print(val)
    # #
    # # response2 = notion_client.notion_pages_client.retrieve_page("faee723c-002f-445e-ad3a-d943dbcd5811")
    # # print(response2)
    # # for value in response["properties"].values():
    # #     print(value)
    #
    # # response2 = notion_database_provider.get_database("1a91e289d5d9470d9e30ff1dfde63c60")
    # # # print(response2)
    # # for val in response2.properties:
    # #     print(val)
