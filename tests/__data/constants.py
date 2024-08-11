# constants.py

from datetime import datetime, timezone
import uuid

# Object constants
OBJECT_ID = uuid.UUID("c02fc1d3-db8b-45c5-a222-27595b15aea7")
PARENT_TYPE = "page_id"
PARENT_PAGE_ID = uuid.UUID("59833787-2cf9-4fdf-8782-e53db20768a5")
CREATED_TIME = datetime(2022, 3, 1, 19, 5, tzinfo=timezone.utc)
LAST_EDITED_TIME = datetime(2022, 7, 6, 19, 41, tzinfo=timezone.utc)
CREATED_BY_ID = uuid.UUID("ee5f0f84-409a-440f-983a-a5315961c6e4")
LAST_EDITED_BY_ID = uuid.UUID("ee5f0f84-409a-440f-983a-a5315961c6e4")
COVER = None
ICON_TYPE = "external"
ICON_URL = "https://www.notion.so/icons/target_gray.svg"
URL = "https://www.notion.so/1a91e289d5d9470d9e30ff1dfde63c60"
PUBLIC_URL = None
