from pydantic import HttpUrl

from block.block_types.BlockTypeDTO import BlockTypeDTO


class ImageDTO(BlockTypeDTO):
    url: HttpUrl
    caption: str
