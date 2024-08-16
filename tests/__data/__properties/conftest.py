# Standard Library
from typing import Any, Dict

# Third Party
import pytest

from .constants import *


@pytest.fixture
def property_data(faker):
    def return_block_data(property_type, property_type_specific_data) -> Dict[str, Any]:
        return {
            "id": PROPERTY_ID,
            "type": property_type,
            "name": faker.unique.word(),
            property_type.value: property_type_specific_data,
        }

    return return_block_data
