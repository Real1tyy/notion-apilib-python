from enum import Enum


class PagePropertyType(Enum):
    """
    Enum representing the possible types of properties in a Notion page object.
    """
    CHECKBOX = "checkbox"
    CREATED_BY = "created_by"
    CREATED_TIME = "created_time"
    DATE = "date"
    EMAIL = "email"
    FILES = "files"
    FORMULA = "formula"
    LAST_EDITED_BY = "last_edited_by"
    LAST_EDITED_TIME = "last_edited_time"
    MULTI_SELECT = "multi_select"
    NUMBER = "number"
    PEOPLE = "people"
    PHONE_NUMBER = "phone_number"
    RELATION = "relation"
    ROLLUP = "rollup"
    RICH_TEXT = "rich_text"
    SELECT = "select"
    STATUS = "status"
    TITLE = "title"
    URL = "url"
    UNIQUE_ID = "unique_id"
    VERIFICATION = "verification"
