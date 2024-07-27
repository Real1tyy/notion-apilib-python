from pydantic import HttpUrl

from block_types.BlockTypeDTO import BlockTypeDTO


class BookmarkDTO(BlockTypeDTO):
    url: HttpUrl
    caption: str
