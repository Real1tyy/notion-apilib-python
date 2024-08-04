# Standard Library
from datetime import datetime
from typing import Optional
from uuid import UUID

# Third Party
from pydantic import BaseModel


class DatabaseMention(BaseModel):
    id: UUID


class DateMention(BaseModel):
    start: datetime
    end: Optional[datetime] = None


class LinkPreviewMention(BaseModel):
    url: str


class PageMention(BaseModel):
    id: UUID


class TemplateMentionDate(BaseModel):
    type: str
    template_mention_date: str


class TemplateMentionUser(BaseModel):
    type: str
    template_mention_user: str


class TemplateMention(BaseModel):
    type: str
    template_mention_date: Optional[TemplateMentionDate] = None
    template_mention_user: Optional[TemplateMentionUser] = None


class UserMention(BaseModel):
    object: str
    id: UUID


class Mention(BaseModel):
    type: str
    database: Optional[DatabaseMention] = None
    date: Optional[DateMention] = None
    link_preview: Optional[LinkPreviewMention] = None
    page: Optional[PageMention] = None
    template_mention: Optional[TemplateMention] = None
    user: Optional[UserMention] = None
