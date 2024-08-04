from typing import Optional


def create_mention(
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
        type=mention_type,
        database=database,
        date=date,
        link_preview=link_preview,
        page=page,
        template_mention=template_mention,
        user=user
    )
