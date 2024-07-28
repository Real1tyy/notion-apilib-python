from pydantic import HttpUrl

from Block import Block


class Pdf(Block):
    url: HttpUrl
    caption: str
