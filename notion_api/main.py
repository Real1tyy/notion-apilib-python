# Third Party
import os

from dotenv import load_dotenv

from data.structures import create_parent
from data.blocks import create_basic_heading1, Heading1
from data.properties import *
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
    blocks_provider = notion.get_block_provider()
    database_provider = notion.get_database_provider()
    page_provider = notion.get_page_provider()
    # parent = create_parent("page_id", "fa0bec9897ef4abba867f0c16513561c")
    #
    # heading1 = create_basic_heading1(parent, "Heading 1", False)
    # create_and_print(heading1, blocks_provider)
    # paragraph = create_basic_paragraph(parent, "Database")

    file_path = "links"

    with open(file_path, "r") as file:
        lines = file.readlines()
    for line in lines:
        database_id = line.rstrip()
        database = database_provider.retrieve_database(database_id)
        # print(len(database.pages))
        break
