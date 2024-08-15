import pytest
from typing import Dict, Any
from .constants import *


@pytest.fixture
def property_data():
    def return_block_data(property_type, property_type_specific_data) -> Dict[str, Any]:
        return {
            "id": PROPERTY_ID,
            "type": property_type,
            "name": PROPERTY_NAME,
            property_type.value: property_type_specific_data,
        }

    return return_block_data
