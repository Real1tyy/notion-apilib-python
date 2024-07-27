from pydantic import HttpUrl

from BlockDTO import BlockDTO


class VideoDTO(BlockDTO):
    url: HttpUrl
    caption: str
