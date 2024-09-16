# Standard Library
from typing import Callable, Type

# First Party
from notion_apilib.data.blocks import Block

from .assertions import assert_serialization_to_json, create_block_object, extract_block_data


def extract_create_assert_structure(data_provider, block_class: Type[Block], assert_structure_func: Callable):
    data = extract_block_data(data_provider, block_class)
    block = create_block_object(data, block_class)
    assert_structure_func(block, data)


def extract_create_assert_serialization(data_provider, class_type: Type[Block]):
    data = extract_block_data(data_provider, class_type)
    block = create_block_object(data, class_type)
    assert_serialization_to_json(block, data[class_type.get_payload_property_name()])
