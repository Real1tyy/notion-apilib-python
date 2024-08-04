# Standard Library
from typing import Optional

# Third Party
from pydantic import BaseModel


class Link(BaseModel):
    url: str


class Text(BaseModel):
    content: str
    link: Optional[Link]


def create_text_object(text: str, link: str = None) -> Text:
    return Text(content=text, link=link)
