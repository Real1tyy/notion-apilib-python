# Standard Library
from typing import Optional

from pydantic import BaseModel


# Third Party

class Link(BaseModel):
    url: str


class Text(BaseModel):
    content: str
    link: Optional[Link]


def create_text_object(text: str, link: str = None) -> Text:
    return Text(content=text, link=link)


class Annotations(BaseModel):
    bold: bool
    italic: bool
    strikethrough: bool
    underline: bool
    code: bool
    color: str


def create_basic_annotations_object() -> Annotations:
    return Annotations(bold=False, italic=False, strikethrough=False, underline=False, code=False, color='default')


class RichText(BaseModel):
    type: str
    text: Text = None
    mention: Mention = None
    equation: Equation = None
    annotations: Annotations
    plain_text: str
    href: Optional[str]

    def change_text(self, text: str):
        self.plain_text = text
        if self.text:
            self.text.content = text


def create_basic_rich_text_object(text: str) -> RichText:
    return RichText(
        type='text',
        text=create_text_object(text),
        annotations=create_basic_annotations_object(),
        plain_text=text,
        href=None
    )
