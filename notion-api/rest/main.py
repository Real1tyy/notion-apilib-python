# Third Party
from dotenv import load_dotenv

from Container import Container
from Parent import create_parent
from data.properties.factory import create_date_page

if __name__ == "__main__":
    load_dotenv()
    container: Container = Container()
    container.config.api_key.from_env("NOTION_INTEGRATION_KEY")

    database_provider = container.notion_database_provider()
    blocks_provider = container.notion_block_provider()
    page_provider = container.notion_page_provider()

    file_path = "links"
    parent = create_parent("workspace")
    page = create_date_page(parent, "date", "2021-10-10")

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
    # parent = create_parent('page_id', "b5d1877b3a554a7fbaacf206adb8a0e2")
    # blocks = create_bulleted_list_item(parent, "green", [])
    # print(blocks)

    # database_id = "706cd118dfaf40c288029314d62e2357"
    # result = database_provider.retrieve_database(database_id)
    # database = result.unwrap()
    # result = database_provider.query_database(database)
    # print(database.pages)
    # print(len(database.pages))
