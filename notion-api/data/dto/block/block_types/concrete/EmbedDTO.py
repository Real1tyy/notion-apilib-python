from pydantic import HttpUrl

from block.block_types.BlockTypeDTO import BlockTypeDTO


class EmbedDTO(BlockTypeDTO):
    url: HttpUrl
