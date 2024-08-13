# Third Party
import os

from dotenv import load_dotenv

from notion_api import *
from notion_api.data.properties import *
from type_ import BlockType
from type_factory import deserialize_block


def create_and_print(object, blocks_provider):
    try:
        block = blocks_provider.create_block(object)
        retrieved_block = blocks_provider.retrieve_block(block.unwrap().id)
        print(retrieved_block)
        print(blocks_provider.delete_block(retrieved_block.unwrap()))
    except Exception as e:
        print(e)


DATA = {'object': 'block', 'id': 'c02fc1d3-db8b-45c5-a222-27595b15aea7',
        'parent': {'type': 'page_id', 'page_id': 'fa0bec9897ef4abba867f0c16513561c'},
        'created_time': '2022-03-01T19:05:00+00:00', 'last_edited_time': '2022-07-06T19:41:00+00:00',
        'created_by': {'object': 'user', 'id': 'ee5f0f84-409a-440f-983a-a5315961c6e4'},
        'last_edited_by': {'object': 'user', 'id': 'ee5f0f84-409a-440f-983a-a5315961c6e4'}, 'archived': False,
        'in_trash': False, 'has_children': False, 'type': BlockType.CHILD_PAGE, 'child_page': {'title': 'BEST TITLE'}}

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("NOTION_INTEGRATION_KEY")
    notion = NotionApi(api_key)
    blocks_provider = notion.get_block_provider()
    database_provider = notion.get_database_provider()
    page_provider = notion.get_page_provider()
    block = deserialize_block(DATA)
    # json = block.serialize_to_json()
    # print(json)
    # blocks_provider.create_block(block)

    # parent = create_parent("page_id", "fa0bec9897ef4abba867f0c16513561c")
    print(database_provider.retrieve_database("97b48d4fece741b395ce37ec64e93346").created_by)

    # heading1 = create_basic_heading1(parent, "Heading 1", False)
    # create_and_print(heading1, blocks_provider)
    # paragraph = create_basic_paragraph(parent, "Database")
