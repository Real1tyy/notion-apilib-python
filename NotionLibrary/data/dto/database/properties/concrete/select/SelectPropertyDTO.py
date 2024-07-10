from typing import Any

from database.properties.PropertyDTO import PropertyDTO


class SelectPropertyDTO(PropertyDTO):
    options: dict[str, Any]
