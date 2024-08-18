# constants.py

# Standard Library
import uuid
from datetime import datetime, timezone

# Object constants
USER_TYPES = ["person", "bot"]
USER_ID = uuid.UUID("c02fc1d3-db8b-45c5-a222-27595b15aea7")
USER_AVATAR_URL = "https://www.notion.so/images/user.png"
USER_NAME = "UserName"
PARENT_TYPES = ["page_id", "database_id", "block_id", "workspace"]
PARENT_PAGE_ID = uuid.UUID("59833787-2cf9-4fdf-8782-e53db20768a5")
PARENT_DATABASE_ID = uuid.UUID("59833787-2cf9-4fdf-8782-e53db20768a5")
PARENT_BLOCK_ID = uuid.UUID("59833787-2cf9-4fdf-8782-e53db20768a5")
RICH_TEXT_TYPE = ["text", "mention", "equation"]
RICH_TEXT_CONTENT = "Lacinato kale"
RICH_TEXT_COLOR = "green"
RICH_TEXT_URL = "https://www.notion.so"
TEXT_LINK = "https://www.notion.so"
EQUATION_EXPRESSION = "a^2 + b^2 = c^2"
EMOJI_TYPE = "emoji"
EMOJI_EMOJI = "🥬"
MENTION_USER_ID = uuid.UUID("c02fc1d3-db8b-45c5-a222-27595b15aea7")
ICON_URL = "https://www.notion.so/icons/target_gray.svg"
ICON_EXPIRY_TIME = datetime(2022, 3, 1, 19, 5, tzinfo=timezone.utc)
RESOURCE_TYPE = ["external", "file"]
HREF_OPTIONS = ["https://www.notion.so", None]
MENTION_TYPES = ["database", "page", "user", "date", "link_preview", "template_mention"]
MENTION_DATABASE_ID = uuid.UUID("59833787-2cf9-4fdf-8782-e53db20768a5")
MENTION_DATE_START = datetime(2022, 3, 1, 19, 5, tzinfo=timezone.utc)
MENTION_DATE_END_OPTIONS = [datetime(2022, 3, 10, 19, 5, tzinfo=timezone.utc), None]
MENTION_LINK_PREVIEW = "https://www.notion.so/images/user.png"
MENTION_PAGE_ID = uuid.UUID("59833787-2cf9-4fdf-8782-e53db20768a5")
TEMPLATE_MENTION_OPTIONS = ["template_mention_date", "template_mention_user"]
TEMPLATE_MENTION_DATE_OPTIONS = ["today", "now"]
TEMPLATE_MENTION_USER_OPTIONS = ["me"]
