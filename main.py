# Standard Library
import os

# Third Party
from dotenv import load_dotenv

from notion_api import *


if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("NOTION_INTEGRATION_KEY")
    notion = NotionApi(api_key)
    blocks_provider = notion.get_block_provider()
    database_provider = notion.get_database_provider()
    page_provider = notion.get_page_provider()
    print(database_provider.retrieve_database("97b48d4fece741b395ce37ec64e93346"))
