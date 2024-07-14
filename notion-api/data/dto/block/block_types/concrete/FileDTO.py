from pydantic import HttpUrl

from block.block_types.BlockTypeDTO import BlockTypeDTO


class FileDTO(BlockTypeDTO):
    url: HttpUrl
    caption: str
