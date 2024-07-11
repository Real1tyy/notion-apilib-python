from typing import Any

from database.properties.PropertyDTO import PropertyDTO


class MultiSelectPropertyDTO(PropertyDTO):
    options: dict[str, Any]
