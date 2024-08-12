from typing import TypeVar, Type, Callable

from __block.constants import BLOCK_TYPE
from __data.assertions import assert_object_data_is_correct
from notion_api.data.blocks import Block
from __data.utils.__serialization import transform_dictionary


def assert_block_data_is_correct(data: Block, expected_data: dict):
    assert_object_data_is_correct(data, expected_data)
    assert data.has_children == expected_data["has_children"]
    if "children" in expected_data:
        assert data.children == expected_data["children"]
    else:
        assert data.children == []
    assert data.type == expected_data["type"]


T = TypeVar("T", bound=Block)


def extract_block_data(data_provider: Callable, block_class: Type[T]) -> dict:
    block_type = block_class.get_associated_block_type()
    return data_provider(block_type)


def create_block_object(block_data: dict, block_class: Type[T]) -> T:
    block = block_class(**block_data)
    assert block.__class__ == block_class
    return block


def assert_serialization_to_json(block, block_type_specific_data):
    block_data = transform_dictionary(block_type_specific_data)
    json = block.serialize_to_json()
    assert json["object"] == BLOCK_TYPE
    property_name = block.__class__.get_payload_property_name()
    assert json["type"] == property_name
    if block_type_specific_data != {}:
        print(json[property_name])
        print(block_data)
        assert json[property_name] == block_data
