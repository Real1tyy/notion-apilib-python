# Standard Library
from typing import Optional, Any

# Third Party
from pydantic import BaseModel, model_validator, model_serializer

import notion_apilib.data._structures.factory as factory
from notion_apilib.data import BasicConfiguration
from .mention_ import Mention


class Link(BaseModel):
    """
    Represents a link in the Notion API.

    Attributes
    ----------
    url : str
        The URL of the link.
    """

    url: str


class Text(BaseModel):
    """
    Represents a text object in the Notion API.

    Attributes
    ----------
    content : str
        The content of the text.
    link : Optional[Link]
        An optional link associated with the text.
    """

    content: str
    link: Optional[Link] = None


class Annotations(BaseModel):
    """
    Represents text annotations in the Notion API.

    Attributes
    ----------
    bold : bool
        Indicates if the text is bold.
    italic : bool
        Indicates if the text is italicized.
    strikethrough : bool
        Indicates if the text is strikethrough.
    underline : bool
        Indicates if the text is underlined.
    code : bool
        Indicates if the text is code.
    color : str
        The color of the text.
    """

    bold: bool
    italic: bool
    strikethrough: bool
    underline: bool
    code: bool
    color: str


class EquationStructure(BaseModel):
    """
    Represents an equation structure in the Notion API.

    Attributes
    ----------
    expression : str
        The expression of the equation.
    """

    expression: str


class RichText(BasicConfiguration):
    """
    Represents a rich text object in the Notion API.

    Attributes
    ----------
    type : str
        The type of the rich text.
    text : Text
        The text object.
    mention : Mention
        The mention object.
    equation : Equation
        The equation object.
    annotations : Annotations
        The annotations applied to the text.
    plain_text : str
        The plain text without annotations.
    href : Optional[str]
        An optional hyperlink reference.
    """

    type: str
    text: Optional[Text] = None
    mention: Optional[Mention] = None
    equation: Optional[EquationStructure] = None
    annotations: Annotations
    plain_text: str
    href: Optional[str] = None

    def change_text(self, text: str):
        """
        Change the text content of the rich text object.

        Parameters
        ----------
        text : str
            The new text content.
        """
        self.plain_text = text
        if self.text:
            self.text.content = text


class FormatedText(BasicConfiguration):
    """
    Represents a formatted text object in the Notion API.

    Attributes
    ----------
    rich_text : list[RichText]
        The rich text content.
    """
    rich_text: list[RichText]

    @model_validator(mode="before")
    def parse_rich_text(cls, v: Any):
        result = dict()
        result["rich_text"] = v
        return result

    @model_serializer
    def serialize_rich_text(self) -> list[dict]:
        return [rich_text.json_dump() for rich_text in self.rich_text]

    @property
    def text(self) -> str:
        """
        gets the value of the plain text property, note that the value is returned as a plain text, so any formatting
        is ignored, if you want specific formatting, you should use the title_structure attribute
        :return: plain text value of the title
        """
        return "".join([rich_text.plain_text for rich_text in self.rich_text])

    @text.setter
    def text(self, value: str) -> None:
        """
        sets the value of the text property, note that the value is expected string so plain text,
        meaning no formatting is possible, if you want specific formatting, you should use the rich_text
        attribute directly, also note that any previous value or formatting will be overwritten to plain text
        :param value: value to set - plain text
        :return: None
        """
        self.rich_text = [factory.create_basic_rich_text(value)]

    def __len__(self):
        return len(self.rich_text)

    def __iter__(self):
        return iter(self.rich_text)


__all__ = ["RichText", "Text", "Annotations", "Link", "EquationStructure", "FormatedText"]
