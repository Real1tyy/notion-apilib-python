from pydantic import HttpUrl

from BlockDTO import BlockDTO


class PdfDTO(BlockDTO):
    url: HttpUrl
    caption: str
