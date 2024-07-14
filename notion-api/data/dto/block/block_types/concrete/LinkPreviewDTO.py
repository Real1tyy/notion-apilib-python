from pydantic import HttpUrl

from block.block_types.BlockTypeDTO import BlockTypeDTO


class LinkPreviewDTO(BlockTypeDTO):
    url: HttpUrl
