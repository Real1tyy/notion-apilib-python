from typing import Dict, Any

from database.properties.PropertyDTO import PropertyDTO


class RelationPropertyDTO(PropertyDTO):
    related_to: Dict[str, Any]
