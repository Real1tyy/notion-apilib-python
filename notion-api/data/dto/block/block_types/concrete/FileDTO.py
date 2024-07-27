from pydantic import HttpUrl

from BlockDTO import BlockDTO


class FileDTO(BlockDTO):
    url: HttpUrl
    caption: str
