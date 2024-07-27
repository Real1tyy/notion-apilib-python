from pydantic import HttpUrl

from Block import Block


class Embed(Block):
    url: HttpUrl
