from typing import Optional

from _structures.data import Annotations, Text, RichText, Link, Mention


def create_basic_annotations() -> Annotations:
    return Annotations(bold=False, italic=False, strikethrough=False, underline=False, code=False, color='default')


def create_basic_rich_text(text: str) -> RichText:
    return RichText(
        type='text',
        text=create_text(text),
        annotations=create_basic_annotations(),
        plain_text=text,
        href=None
    )


def create_link(url: str) -> Link:
    """
    Factory method to create a Link.

    Parameters
    ----------
    url : str
        The URL of the link.

    Returns
    -------
    Link
        A new Link instance.
    """
    return Link(url=url)


def create_text(content: str, link: Optional[Link] = None) -> Text:
    """
    Factory method to create a Text object.

    Parameters
    ----------
    content : str
        The content of the text.
    link : Optional[Link]
        An optional link associated with the text. Defaults to None.

    Returns
    -------
    Text
        A new Text instance.
    """
    return Text(content=content, link=link)


def create_annotations(
        bold: bool, italic: bool, strikethrough: bool, underline: bool, code: bool, color: str) -> Annotations:
    """
    Factory method to create an Annotations object.

    Parameters
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

    Returns
    -------
    Annotations
        A new Annotations instance.
    """
    return Annotations(
        bold=bold, italic=italic, strikethrough=strikethrough, underline=underline, code=code, color=color)


def create_rich_text(
        type_: str, annotations: Annotations, plain_text: str, text: Optional[Text] = None,
        mention: Optional[Mention] = None, equation: Optional['Equation'] = None,
        href: Optional[str] = None) -> RichText:
    """
    Factory method to create a RichText object.

    Parameters
    ----------
    type_ : str
        The type of the rich text.
    annotations : Annotations
        The annotations applied to the text.
    plain_text : str
        The plain text without annotations.
    text : Optional[Text]
        The text object. Defaults to None.
    mention : Optional[Mention]
        The mention object. Defaults to None.
    equation : Optional[Equation]
        The equation object. Defaults to None.
    href : Optional[str]
        An optional hyperlink reference. Defaults to None.

    Returns
    -------
    RichText
        A new RichText instance.
    """
    return RichText(
        type=type_,
        text=text,
        mention=mention,
        equation=equation,
        annotations=annotations,
        plain_text=plain_text,
        href=href
    )
