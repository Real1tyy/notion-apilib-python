# mention_factory.py

# Standard Library
from datetime import datetime
from typing import Optional
from uuid import UUID

# First Party
from notion_api.data._structures.data import (
    DatabaseMention,
    DateMention,
    LinkPreviewMention,
    Mention,
    PageMention,
    TemplateMention,
    TemplateMentionDate,
    TemplateMentionUser,
    UserMention,
)


def create_database_mention(id_: UUID) -> DatabaseMention:
    """
    Factory method to create a DatabaseMention.

    Parameters
    ----------
    id_ : UUID
        The ID of the mentioned database.

    Returns
    -------
    DatabaseMention
        A new DatabaseMention instance.
    """
    return DatabaseMention(id=id_)


def create_date_mention(start: datetime, end: Optional[datetime] = None) -> DateMention:
    """
    Factory method to create a DateMention.

    Parameters
    ----------
    start : datetime
        The start date and time.
    end : Optional[datetime]
        The end date and time, if any.

    Returns
    -------
    DateMention
        A new DateMention instance.
    """
    return DateMention(start=start, end=end)


def create_link_preview_mention(url: str) -> LinkPreviewMention:
    """
    Factory method to create a LinkPreviewMention.

    Parameters
    ----------
    url : str
        The URL of the link preview.

    Returns
    -------
    LinkPreviewMention
        A new LinkPreviewMention instance.
    """
    return LinkPreviewMention(url=url)


def create_page_mention(id_: UUID) -> PageMention:
    """
    Factory method to create a PageMention.

    Parameters
    ----------
    id_ : UUID
        The ID of the mentioned page.

    Returns
    -------
    PageMention
        A new PageMention instance.
    """
    return PageMention(id=id_)


def create_template_mention_date(type_: str, template_mention_date: str) -> TemplateMentionDate:
    """
    Factory method to create a TemplateMentionDate.

    Parameters
    ----------
    type_ : str
        The type of the template mention.
    template_mention_date : str
        The template mention date string.

    Returns
    -------
    TemplateMentionDate
        A new TemplateMentionDate instance.
    """
    return TemplateMentionDate(type=type_, template_mention_date=template_mention_date)


def create_template_mention_user(type_: str, template_mention_user: str) -> TemplateMentionUser:
    """
    Factory method to create a TemplateMentionUser.

    Parameters
    ----------
    type_ : str
        The type of the template mention.
    template_mention_user : str
        The template mention user string.

    Returns
    -------
    TemplateMentionUser
        A new TemplateMentionUser instance.
    """
    return TemplateMentionUser(type=type_, template_mention_user=template_mention_user)


def create_template_mention(
        type_: str,
        template_mention_date: Optional[TemplateMentionDate] = None,
        template_mention_user: Optional[TemplateMentionUser] = None) -> TemplateMention:
    """
    Factory method to create a TemplateMention.

    Parameters
    ----------
    type_ : str
        The type of the template mention.
    template_mention_date : Optional[TemplateMentionDate]
        The template mention date object, if any.
    template_mention_user : Optional[TemplateMentionUser]
        The template mention user object, if any.

    Returns
    -------
    TemplateMention
        A new TemplateMention instance.
    """
    return TemplateMention(
        type=type_, template_mention_date=template_mention_date, template_mention_user=template_mention_user)


def create_user_mention(object_: str, id_: UUID) -> UserMention:
    """
    Factory method to create a UserMention.

    Parameters
    ----------
    object_ : str
        The object type (always 'user').
    id_ : UUID
        The ID of the mentioned user.

    Returns
    -------
    UserMention
        A new UserMention instance.
    """
    return UserMention(object=object_, id=id_)


def create_mention(
        type_: str,
        database: Optional[DatabaseMention] = None,
        date: Optional[DateMention] = None,
        link_preview: Optional[LinkPreviewMention] = None,
        page: Optional[PageMention] = None,
        template_mention: Optional[TemplateMention] = None,
        user: Optional[UserMention] = None) -> Mention:
    """
    Factory method to create a Mention.

    Parameters
    ----------
    type_ : str
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

    Returns
    -------
    Mention
        A new Mention instance.
    """
    return Mention(
        type=type_,
        database=database,
        date=date,
        link_preview=link_preview,
        page=page,
        template_mention=template_mention,
        user=user
    )


__all__ = ['create_mention', 'create_user_mention', 'create_template_mention', 'create_page_mention',
           'create_date_mention', 'create_link_preview_mention', 'create_database_mention',
           'create_template_mention_user', 'create_template_mention_date']
