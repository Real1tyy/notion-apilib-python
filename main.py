# Standard Library
import os

# Third Party
from dotenv import load_dotenv

from notion_api import *
from notion_api.data import *
from notion_api.data.blocks import *
from notion_api.data.properties import *
from notion_api.data.structures import *

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("NOTION_INTEGRATION_KEY")
    notion = NotionApi(api_key)
    blocks_provider = notion.block_provider
    database_provider = notion.database_provider
    page_provider = notion.page_provider
    data = database_provider.retrieve_database("97b48d4fece741b395ce37ec64e93346")
    print(data.icon)
    print(data.cover)
    print(data.properties)
    print(data.to_json_string())
