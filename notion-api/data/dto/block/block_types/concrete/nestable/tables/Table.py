from Block import Block


class Table(Block):
    has_column_header: bool
    has_row_header: bool
    table_width: int
    children: list
