from pydantic import HttpUrl

from block_types.BlockTypeDTO import BlockTypeDTO


class BookmarkBlockDTO(BlockTypeDTO):
    url: HttpUrl
    caption: str
