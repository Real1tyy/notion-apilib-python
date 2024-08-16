# constants.py

# Standard Library
import uuid
from datetime import datetime, timezone

# Object constants
OBJECT_ID = uuid.UUID("c02fc1d3-db8b-45c5-a222-27595b15aea7")
CREATED_TIME = datetime(2022, 3, 1, 19, 5, tzinfo=timezone.utc)
LAST_EDITED_TIME = datetime(2022, 7, 6, 19, 41, tzinfo=timezone.utc)
CREATED_BY_ID = uuid.UUID("ee5f0f84-409a-440f-983a-a5315961c6e4")
LAST_EDITED_BY_ID = uuid.UUID("ee5f0f84-409a-440f-983a-a5315961c6e4")
COVER = None
URL = "https://www.notion.so/1a91e289d5d9470d9e30ff1dfde63c60"
PUBLIC_URL = None
OBJECT_TYPES = ["page", "database", "block", "workspace"]
