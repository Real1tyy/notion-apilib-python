from block.block_types.BlockTypeDTO import BlockTypeDTO


class ToDoDTO(BlockTypeDTO):
    text: str
    checked: bool
