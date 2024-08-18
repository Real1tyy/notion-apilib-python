# Standard Library
from typing import Literal

parents_types = Literal["database_id", "page_id", "block_id", "workspace"]

file_type = Literal["external", "file"]

__all__ = ["parents_types", "file_type"]
