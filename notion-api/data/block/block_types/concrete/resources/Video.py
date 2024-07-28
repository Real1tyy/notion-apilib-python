from pydantic import HttpUrl

from Block import Block


class Video(Block):
    url: HttpUrl
    caption: str
