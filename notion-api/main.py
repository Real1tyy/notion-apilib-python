# Third Party
from dotenv import load_dotenv

from data.blocks import *
from data.properties import *
from notion import Container, NotionApi

if __name__ == "__main__":
    load_dotenv()
    # yx = create_concrete_block_type("da")
    # z = create_date_page("da", "Date", "2021-10-10")
    #
    notion = NotionApi("secret_iptuPR2jz8YNka3cHhIPEwQJDRspoI9VxcUBZkN8pca")
    y = notion.get_pages_provider()
    x = notion.get_pages_provider()
    print(x.retrieve_page("b5d1877b3a554a7fbaacf206adb8a0e2"))

    # container: Container = Container()
    # container.config.api_key.from_env("NOTION_INTEGRATION_KEY")

    # database_provider = container.notion_database_provider()
    # blocks_provider = container.notion_block_provider()
    # # page_provider = container.notion_page_provider()
    #
    # file_path = "links"
    # parent = create_parent("workspace")
    # page = create_date_page(parent, "date", "2021-10-10")
    #
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
    # _blocks = create_bulleted_list_item(parent, "green", [])
    # print(_blocks)

    # database_id = "706cd118dfaf40c288029314d62e2357"
    # result = database_provider.retrieve_database(database_id)
    # database = result.unwrap()
    # result = database_provider.query_database(database)
    # print(database.pages)
    # print(len(database.pages))
