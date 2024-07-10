from typing import Dict

from database.properties.PropertyDTO import PropertyDTO


class UniqueIDPropertyDTO(PropertyDTO):
    unique_id: Dict[str, str]
