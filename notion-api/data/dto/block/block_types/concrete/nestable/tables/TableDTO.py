from block.block_types.BlockTypeDTO import BlockTypeDTO


class TableDTO(BlockTypeDTO):
    has_column_header: bool
    has_row_header: bool
    table_width: int
    children: list  # Adjust type as needed
