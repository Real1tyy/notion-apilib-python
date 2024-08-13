from typing import Type, Callable

from .assertions import extract_block_data, create_block_object, assert_serialization_to_json
from notion_api.data.blocks import Block


def extract_create_assert_structure(data_provider, block_class: Type[Block], assert_structure_func: Callable):
    data = extract_block_data(data_provider, block_class)
    block = create_block_object(data, block_class)
    assert_structure_func(block, data)


def extract_create_assert_serialization(data_provider, class_type: Type[Block]):
    data = extract_block_data(data_provider, class_type)
    block = create_block_object(data, class_type)
    assert_serialization_to_json(block, data[class_type.get_associated_block_type().value])
