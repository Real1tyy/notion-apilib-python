# Standard Library
from typing import Any

# Third Party
from _properties.property import DatabaseProperty, PageProperty
from structures import RichText
from _properties.type_ import PropertyType


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
        title (list[RichText]): The title content of the page property.
    """
    title: list[RichText]

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
