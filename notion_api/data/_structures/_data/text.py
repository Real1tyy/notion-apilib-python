# Standard Library
from typing import Optional

# Third Party
from pydantic import BaseModel


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


class RichText(BaseModel, arbitrary_types_allowed=True):
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
    mention: Optional['Mention'] = None
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


__all__ = ['RichText', 'Text', 'Annotations', 'Link', 'EquationStructure']
