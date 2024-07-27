from pydantic import HttpUrl

from BlockDTO import BlockDTO


class LinkPreviewDTO(BlockDTO):
    url: HttpUrl
