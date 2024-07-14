from pydantic import HttpUrl

from block.block_types.BlockTypeDTO import BlockTypeDTO


class VideoDTO(BlockTypeDTO):
    url: HttpUrl
    caption: str
