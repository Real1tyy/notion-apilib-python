# Third Party
import os

from dotenv import load_dotenv
from notion_api import *
from notion_api.data.properties import *


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
    filters = [create_select_filter_equals("Type", "Never Ending"), create_timestamp_filter(
        "created_time",
        create_relative_date_filter(
            "whatever",
            "past_month"))]
    and_filter = create_and_filter(filters)
    # or_filter = create_or_filter(filters)
    # and_filter.add_nested_filter_object(or_filter)
    print(and_filter.to_json_string())
    database = database_provider.retrieve_database("1a91e289d5d9470d9e30ff1dfde63c60")
    database = database_provider.query_database(database, and_filter)
    print(len(database.pages))
    filters = [create_select_filter_equals("Type", "Never Ending")]
    and_filter = create_and_filter(filters)
    database = database_provider.query_database(database, and_filter)
    print(len(database.pages))

    # file_path = "links"
    #
    # with open(file_path, "r") as file:
    #     lines = file.readlines()
    # for line in lines:
    #     database_id = line.rstrip()
    #     database = database_provider.retrieve_database(database_id)
    #     # print(len(database.pages))
    #     break
