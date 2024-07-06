from enum import Enum


class PropertyTypes(str, Enum):
    TEXT = "text"
    NUMBER = "number"
    SELECT = "select"
    MULTI_SELECT = "multi-select"
    STATUS = "status"
    DATE = "date"
    PERSON = "person"
    FILES_MEDIA = "files-media"
    CHECKBOX = "checkbox"
    URL = "url"
    EMAIL = "email"
    PHONE = "phone"
    FORMULA = "formula"
    RELATION = "relation"
    ROLLUP = "rollup"
    CREATED_TIME = "created-time"
    CREATED_BY = "created-by"
    LAST_EDITED_TIME = "last-edited-time"
    LAST_EDITED_BY = "last-edited-by"
    BUTTON = "button"
    ID = "id"
