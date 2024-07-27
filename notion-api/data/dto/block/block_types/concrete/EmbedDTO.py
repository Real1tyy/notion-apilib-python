from pydantic import HttpUrl

from BlockDTO import BlockDTO


class EmbedDTO(BlockDTO):
    url: HttpUrl
