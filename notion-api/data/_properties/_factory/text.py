from RichText import RichText
from _properties.type import PropertyType
from database import Database
from general import _create_page_property, _create_database_property
from page import Page
from text import TitlePage, RichTextPage, RichTextDatabase, TitleDatabase


def create_rich_text_page(
        parent: Page, name: str, rich_text: list[RichText]) -> RichTextPage:
    """
    Factory method to create a RichTextPage object.

    Parameters:
        parent (Page): The parent page to which this rich text property belongs.
        name (str): The name of the rich text property.
        rich_text (list[RichText]): The rich text content of the property.

    Returns:
        RichTextPage: A new RichTextPage object.
    """
    return _create_page_property(
        RichTextPage,
        parent=parent,
        property_type=PropertyType.RICH_TEXT,
        name=name,
        rich_text=rich_text
    )


def create_rich_text_database(
        parent: Database, name: str, rich_text: list[RichText]) -> RichTextDatabase:
    """
    Factory method to create a RichTextDatabase object.

    Parameters:
        parent (Database): The parent database to which this rich text property belongs.
        name (str): The name of the rich text property.
        rich_text (list[RichText]): The rich text content of the property.

    Returns:
        RichTextPage: A new RichTextDatabase object.
    """
    return _create_database_property(
        RichTextDatabase,
        parent=parent,
        property_type=PropertyType.RICH_TEXT,
        name=name,
        rich_text=rich_text
    )


def create_title_page(
        parent: Page, name: str, title: list[RichText]) -> TitlePage:
    """
    Factory method to create a TitlePage object.

    Parameters:
        parent (Page): The parent page to which this title property belongs.
        name (str): The name of the title property.
        title (list[RichText]): The title content of the property.

    Returns:
        TitlePage: A new TitlePage object.
    """
    return _create_page_property(
        TitlePage,
        parent=parent,
        property_type=PropertyType.TITLE,
        name=name,
        title=title
    )


def create_title_database(
        parent: Database, name: str) -> TitleDatabase:
    """
    Factory method to create a TitleDatabase object.

    Parameters:
        parent (Database): The parent database to which this title property belongs.
        name (str): The name of the title property.

    Returns:
        TitleDatabase: A new TitleDatabase object.
    """
    return _create_database_property(
        TitleDatabase,
        parent=parent,
        property_type=PropertyType.TITLE,
        name=name,
        title={}
    )
