from typing import Optional

from pydantic import BaseModel


class Text(BaseModel):
    content: str
    link: Optional[str]


def create_text_object(text: str, link: str = None) -> Text:
    return Text(content=text, link=link)
