from block.block_types.BlockTypeDTO import BlockTypeDTO


class HeadingDTO(BlockTypeDTO):
    rich_text: str
    color: Color
    is_toggleable: bool
