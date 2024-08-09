# Third Party
import os

from dotenv import load_dotenv

from data.structures import create_parent
from data.blocks import create_basic_heading1, Heading1
from data._properties._factory.time import *
from notion import NotionApi
from data import *


def create_and_print(object, blocks_provider):
    try:
        block = blocks_provider.create_block(object)
        retrieved_block = blocks_provider.retrieve_block(block.unwrap().id)
        print(retrieved_block)
        print(blocks_provider.delete_block(retrieved_block.unwrap()))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("NOTION_INTEGRATION_KEY")
    notion = NotionApi(api_key)
    blocks_provider = notion.get_blocks_provider()
    parent = create_parent("page_id", "fa0bec9897ef4abba867f0c16513561c")

    heading1 = create_basic_heading1(parent, "Heading 1", False)
    create_and_print(heading1, blocks_provider)

    # paragraph = create_basic_paragraph(parent, "Database")
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
