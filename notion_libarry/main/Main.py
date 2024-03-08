import os

from dotenv import load_dotenv
from requests import Response

from main.data.Page import Page
from main.rest_api.NotionClient import NotionClient

load_dotenv()

NOTION_INTEGRATION_KEY = os.getenv("NOTION_INTEGRATION_KEY")
DATABASE_ID = "1a91e289d5d9470d9e30ff1dfde63c60"

notion_client = NotionClient(NOTION_INTEGRATION_KEY)
response: Response = notion_client.get_page("c8e3505e2341488e9462542023f599cd")
# print(response.json())

page: Page = Page(**response.json())
# print("\n\n")
print(page)

# url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

# # Headers for authentication and specifying the Notion API version
# headers = {
#         "Authorization": f"Bearer {NOTION_INTEGRATION_KEY}",
#         "Notion-Version": "2022-06-28",
#         "Content-Type": "application/json"
# }
#
# # Example body for filtering and sorting (customize as per your requirement)
# data = {
#         "filter": {
#                 "property": "Name",
#                 "text": {
#                         "contains": "example"
#                 }
#         },
#         "sorts": [
#                 {
#                         "property": "Name",
#                         "direction": "ascending"
#                 }
#         ]
# }
#
# # Make the API request
# response = requests.post(url, headers=headers, data={})
#
# # Check if the request was successful
# if response.status_code == 200:
#     page_details = response.json()
#
#     print("Page Details:", page_details)
# else:
#     print(f"Failed to fetch page details. Status Code: {response.status_code}")
#
# if __name__ == "__main__":
#     load_dotenv()  # This loads the variables from .env
#     # main()
