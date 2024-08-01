from datetime import datetime
from typing import Optional
from uuid import UUID

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


class MentionAttributes(BaseModel):
    type: str
    database: Optional[DatabaseMention] = None
    date: Optional[DateMention] = None
    link_preview: Optional[LinkPreviewMention] = None
    page: Optional[PageMention] = None
    template_mention: Optional[TemplateMention] = None
    user: Optional[UserMention] = None


class Mention(BaseModel):
    mention: MentionAttributes


def create_mention_object(
        mention_type: str,
        database: Optional[DatabaseMention] = None,
        date: Optional[DateMention] = None,
        link_preview: Optional[LinkPreviewMention] = None,
        page: Optional[PageMention] = None,
        template_mention: Optional[TemplateMention] = None,
        user: Optional[UserMention] = None
) -> Mention:
    """
    Factory method to create a Mention object.

    Parameters:
        mention_type (str): The type of the mention.
        database (Optional[DatabaseMention]): The database mention details.
        date (Optional[DateMention]): The date mention details.
        link_preview (Optional[LinkPreviewMention]): The link preview mention details.
        page (Optional[PageMention]): The page mention details.
        template_mention (Optional[TemplateMention]): The template mention details.
        user (Optional[UserMention]): The user mention details.

    Returns:
        Mention: A newly created Mention object.
    """
    return Mention(
        mention=MentionAttributes(
            type=mention_type,
            database=database,
            date=date,
            link_preview=link_preview,
            page=page,
            template_mention=template_mention,
            user=user
        )
    )
