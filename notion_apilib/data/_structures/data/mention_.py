# Standard Library
from datetime import datetime
from typing import Any, Optional
from uuid import UUID

# Third Party
from pydantic import BaseModel, model_validator

from notion_apilib.data._util import check_if_exactly_one_not_none_val


class DatabaseMention(BaseModel):
    """
    Represents a mention of a database in the Notion API.

    Attributes
    ----------
    id : UUID
        The ID of the mentioned database.
    """

    id: UUID


class DateMention(BaseModel):
    """
    Represents a mention of a date in the Notion API.

    Attributes
    ----------
    start : datetime
        The start date and time.
    end : Optional[datetime]
        The end date and time, if any.
    """

    start: datetime
    end: Optional[datetime] = None


class LinkPreviewMention(BaseModel):
    """
    Represents a mention of a link preview in the Notion API.

    Attributes
    ----------
    url : str
        The URL of the link preview.
    """

    url: str


class PageMention(BaseModel):
    """
    Represents a mention of a page in the Notion API.

    Attributes
    ----------
    id : UUID
        The ID of the mentioned page.
    """

    id: UUID


class TemplateMentionDate(BaseModel):
    """
    Represents a template mention of a date in the Notion API.

    Attributes
    ----------
    type : str
        The type of the template mention.
    template_mention_date : str
        The template mention date string.
    """

    template_mention_date: str


class TemplateMentionUser(BaseModel):
    """
    Represents a template mention of a user in the Notion API.

    Attributes
    ----------
    type : str
        The type of the template mention.
    template_mention_user : str
        The template mention user string.
    """

    template_mention_user: str


class TemplateMention(BaseModel):
    """
    Represents a template mention in the Notion API.

    Attributes
    ----------
    type : str
        The type of the template mention.
    template_mention_date : Optional[TemplateMentionDate]
        The template mention date object, if any.
    template_mention_user : Optional[TemplateMentionUser]
        The template mention user object, if any.
    """

    type: str
    template_mention_date: Optional[str] = None
    template_mention_user: Optional[str] = None

    @classmethod
    @model_validator(mode="after")
    def parse_properties(cls, v: Any):
        properties = [v.template_mention_date, v.template_mention_user]
        if check_if_exactly_one_not_none_val(properties):
            raise ValueError(f"Only one of the values from: {properties} can be provided.")
        return v


class UserMention(BaseModel):
    """
    Represents a mention of a user in the Notion API.

    Attributes
    ----------
    object : str
        The object type (always 'user').
    id : UUID
        The ID of the mentioned user.
    """

    object: str
    id: UUID


class Mention(BaseModel):
    """
    Represents a mention in the Notion API.

    Attributes
    ----------
    type : str
        The type of the mention.
    database : Optional[DatabaseMention]
        The database mention object, if any.
    date : Optional[DateMention]
        The date mention object, if any.
    link_preview : Optional[LinkPreviewMention]
        The link preview mention object, if any.
    page : Optional[PageMention]
        The page mention object, if any.
    template_mention : Optional[TemplateMention]
        The template mention object, if any.
    user : Optional[UserMention]
        The user mention object, if any.
    """

    type: str
    database: Optional[DatabaseMention] = None
    date: Optional[DateMention] = None
    link_preview: Optional[LinkPreviewMention] = None
    page: Optional[PageMention] = None
    template_mention: Optional[TemplateMention] = None
    user: Optional[UserMention] = None

    @classmethod
    @model_validator(mode="after")
    def parse_properties(cls, v: Any):
        properties = [
            v.database,
            v.date,
            v.link_preview,
            v.page,
            v.template_mention,
            v.user,
        ]
        if check_if_exactly_one_not_none_val(properties):
            raise ValueError(f"Only one of the values from: {properties} can be provided.")
        return v


__all__ = [
    "Mention",
    "UserMention",
    "TemplateMention",
    "TemplateMentionUser",
    "TemplateMentionDate",
    "LinkPreviewMention",
    "DateMention",
    "DatabaseMention",
    "PageMention",
]
