from datetime import datetime
from typing import Optional, Annotated
from uuid import UUID

from pydantic import BaseModel
from pydantic.types import UuidVersion


class DatabaseMention(BaseModel):
    id: Annotated[UUID, UuidVersion(4)]


class DateMention(BaseModel):
    start: datetime
    end: Optional[datetime] = None


class LinkPreviewMention(BaseModel):
    url: str


class PageMention(BaseModel):
    id: Annotated[UUID, UuidVersion(4)]


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
    id: Annotated[UUID, UuidVersion(4)]


class Mention(BaseModel):
    type: str
    database: Optional[DatabaseMention] = None
    date: Optional[DateMention] = None
    link_preview: Optional[LinkPreviewMention] = None
    page: Optional[PageMention] = None
    template_mention: Optional[TemplateMention] = None
    user: Optional[UserMention] = None
