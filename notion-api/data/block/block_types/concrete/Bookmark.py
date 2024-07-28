from pydantic import BaseModel

from Block import Block


class BookmarkAttributes(BaseModel):
    url: str
    caption: list[str]


class Bookmark(Block):
    bookmark: BookmarkAttributes
