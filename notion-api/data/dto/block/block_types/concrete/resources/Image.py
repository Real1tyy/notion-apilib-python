from pydantic import HttpUrl

from Block import Block


class Image(Block):
    url: HttpUrl
    caption: str
