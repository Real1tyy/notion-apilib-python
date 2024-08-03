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
    # with open(file_path, "r") as file:
    #     lines = file.readlines()
    # for line in lines:
    #     if line != lines[4]:
    #         continue
    #
    # database_id = "773d05244a8645e3890e00d9f0c000fb"
    # result = database_provider.retrieve_database(database_id)
    # database = result.unwrap()
    # result = database_provider.query_database(database)
    # print(database.pages)
    # print(len(database.pages))
    #
    database_id = "aa9c9ea5b03b436e92a91edea5f69b19"
    result = database_provider.retrieve_database(database_id)
    database = result.unwrap()
    result = database_provider.query_database(database)
    print(database.pages)
    print(len(database.pages))
