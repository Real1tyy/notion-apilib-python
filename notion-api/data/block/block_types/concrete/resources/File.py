from pydantic import HttpUrl

from Block import Block


class File(Block):
    url: HttpUrl
    caption: str
