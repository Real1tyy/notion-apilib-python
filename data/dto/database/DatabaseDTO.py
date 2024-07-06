from typing import Annotated

from MajorObjectDTO import MajorObjectDTO
from validators import attributes_validator


class DatabaseDTO(MajorObjectDTO):
    title: Annotated[str, attributes_validator]
    description: Annotated[str, attributes_validator]
    is_inline: bool
