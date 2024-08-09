# Standard Library
from enum import Enum


class PropertyType(str, Enum):
    """
    Enum representing the various types of properties in the Notion API.

    Attributes
    ----------
    TITLE : str
        Represents a title property.
    RICH_TEXT : str
        Represents a rich text property.
    NUMBER : str
        Represents a number property.
    SELECT : str
        Represents a select property.
    MULTI_SELECT : str
        Represents a multi-select property.
    DATE : str
        Represents a date property.
    PEOPLE : str
        Represents a people property.
    FILES : str
        Represents a files property.
    CHECKBOX : str
        Represents a checkbox property.
    URL : str
        Represents a URL property.
    EMAIL : str
        Represents an email property.
    PHONE_NUMBER : str
        Represents a phone number property.
    FORMULA : str
        Represents a formula property.
    RELATION : str
        Represents a relation property.
    ROLLUP : str
        Represents a rollup property.
    CREATED_TIME : str
        Represents a created time property.
    CREATED_BY : str
        Represents a created by property.
    LAST_EDITED_TIME : str
        Represents a last edited time property.
    LAST_EDITED_BY : str
        Represents a last edited by property.
    UNIQUE_ID : str
        Represents a unique ID property.
    STATUS : str
        Represents a status property.
    """
    TITLE = "title"
    RICH_TEXT = "rich_text"
    NUMBER = "number"
    SELECT = "select"
    MULTI_SELECT = "multi_select"
    DATE = "date"
    PEOPLE = "people"
    FILES = "files"
    CHECKBOX = "checkbox"
    URL = "url"
    EMAIL = "email"
    PHONE_NUMBER = "phone_number"
    FORMULA = "formula"
    RELATION = "relation"
    ROLLUP = "rollup"
    CREATED_TIME = "created_time"
    CREATED_BY = "created_by"
    LAST_EDITED_TIME = "last_edited_time"
    LAST_EDITED_BY = "last_edited_by"
    UNIQUE_ID = "unique_id"
    STATUS = "status"
