from BlockDTO import BlockDTO


class TableDTO(BlockDTO):
    has_column_header: bool
    has_row_header: bool
    table_width: int
    children: list
