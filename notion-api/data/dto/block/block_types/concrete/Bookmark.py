from pydantic import HttpUrl

from Block import Block


class Bookmark(Block):
    url: HttpUrl
    caption: list[str]
