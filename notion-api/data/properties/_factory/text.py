from typing import Optional

from Page import Page
from PropertyType import PropertyType
from RichText import RichText
from TextProperty import TitlePage, RichTextPage
from factory.general import _create_page_property


def create_rich_text_page(
        parent: Page, name: str, rich_text: list[RichText], id_: Optional[str] = None) -> RichTextPage:
    """
    Factory method to create a RichTextPage object.

    Parameters:
        parent (Page): The parent page to which this rich text property belongs.
        name (str): The name of the rich text property.
        rich_text (list[RichText]): The rich text content of the property.
        id_ (Optional[str]): The optional ID of the rich text property.

    Returns:
        RichTextPage: A new RichTextPage object.
    """
    return _create_page_property(
        RichTextPage,
        parent=parent,
        property_type=PropertyType.RICH_TEXT,
        name=name,
        id_=id_,
        rich_text=rich_text
    )


def create_title_page(
        parent: Page, name: str, title: list[RichText], id_: Optional[str] = None) -> TitlePage:
    """
    Factory method to create a TitlePage object.

    Parameters:
        parent (Page): The parent page to which this title property belongs.
        name (str): The name of the title property.
        title (list[RichText]): The title content of the property.
        id_ (Optional[str]): The optional ID of the title property.

    Returns:
        TitlePage: A new TitlePage object.
    """
    return _create_page_property(
        TitlePage,
        parent=parent,
        property_type=PropertyType.TITLE,
        name=name,
        id_=id_,
        title=title
    )
