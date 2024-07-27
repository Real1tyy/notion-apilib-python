from pydantic import HttpUrl

from Block import Block


class LinkPreview(Block):
    url: HttpUrl
