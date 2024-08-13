# constants.py

from datetime import datetime, timezone
import uuid

# Object constants
USER_ID = uuid.UUID("c02fc1d3-db8b-45c5-a222-27595b15aea7")
USER_AVATAR_URL = "https://www.notion.so/images/user.png"
USER_NAME = "UserName"
PARENT_PAGE_ID = uuid.UUID("59833787-2cf9-4fdf-8782-e53db20768a5")
PARENT_DATABASE_ID = uuid.UUID("59833787-2cf9-4fdf-8782-e53db20768a5")
PARENT_BLOCK_ID = uuid.UUID("59833787-2cf9-4fdf-8782-e53db20768a5")
RICH_TEXT_CONTENT = "Lacinato kale"
RICH_TEXT_COLOR = "green"
TEXT_LINK = "https://www.notion.so"
EQUATION_EXPRESSION = "a^2 + b^2 = c^2"
EMOJI_TYPE = "emoji"
EMOJI_EMOJI = "🥬"
MENTION_USER_ID = uuid.UUID("c02fc1d3-db8b-45c5-a222-27595b15aea7")
ICON_URL = "https://www.notion.so/icons/target_gray.svg"
ICON_EXPIRY_TIME = datetime(2022, 3, 1, 19, 5, tzinfo=timezone.utc)
