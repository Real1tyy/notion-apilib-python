# Standard Library
from typing import Any

from pydantic import Field

# First Party
from ..property import DatabaseProperty, PageProperty
from ..type_ import PropertyType
from notion_apilib.data.structures import RichText, create_basic_rich_text


class RichTextPage(PageProperty):
    """
    A model representing a rich text property for a page.

    Attributes:
        rich_text (list[RichText]): The rich text content of the page property.
    """

    rich_text: list[RichText]

    def change_text(self, text: str):
        """
        Change the text of the first rich text element.

        Parameters:
            text (str): The new text to set.
        """
        if len(self.rich_text) > 0:
            self.rich_text[0].change_text(text)

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.RICH_TEXT


class RichTextDatabase(DatabaseProperty):
    """
    A model representing a rich text property for a database.

    Attributes:
        rich_text (dict[str, Any]): The dictionary representing the rich text property for the database.
    """

    rich_text: dict[str, Any]

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.RICH_TEXT


class TitlePage(PageProperty):
    """
    A model representing a title property for a page.

    Attributes:
        title_structure (list[RichText]): The title content of the page property.
    """

    title_structure: list[RichText] = Field(alias="title")

    @property
    def title(self) -> str:
        """
        gets the value of the title Page property, note that the value is returned as a plain text, so any formatting
        is ignored, if you want specific formatting, you should use the title_structure attribute
        :return: plain text value of the title
        """
        return "".join([rich_text.plain_text for rich_text in self.title_structure])

    @title.setter
    def title(self, value: str) -> None:
        """
        sets the value of the title Page property, note that the value is expected to be plain text, so any formatting
        will be ignored, if you want specific formatting, you should use the title_structure attribute, also note
        that any previous value or formatting will be overwritten to plain text
        :param value: value to set - plain text
        :return: None
        """
        self.title_structure = [create_basic_rich_text(value)]

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.TITLE


class TitleDatabase(DatabaseProperty):
    """
    A model representing a title property for a database.

    Attributes:
        title (dict[str, Any]): The dictionary representing the title property for the database.
    """

    title: dict[str, Any]

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.TITLE


__all__ = ["RichTextPage", "RichTextDatabase", "TitlePage", "TitleDatabase"]
