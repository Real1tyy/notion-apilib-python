from pydantic import HttpUrl

from BlockDTO import BlockDTO


class ImageDTO(BlockDTO):
    url: HttpUrl
    caption: str
