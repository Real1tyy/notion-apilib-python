import pytest
from typing import Dict, Any
from tests.__data.__block.constants import *


@pytest.fixture
def block_data(object_data):
    def return_block_data(block_type, block_type_specific_data) -> Dict[str, Any]:
        data = object_data(BLOCK_TYPE)
        block_data = {
            "has_children": False,
            "type": block_type,
            block_type.value: block_type_specific_data,
        }
        data.update(block_data)
        return data

    return return_block_data


@pytest.fixture
def block_text_data(create_rich_text):
    return {
        "rich_text": create_rich_text,
        "color": BLOCK_TEXT_COLOR,
    }
