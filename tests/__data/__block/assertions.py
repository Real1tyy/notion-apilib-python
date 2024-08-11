from typing import TypeVar, Type, Callable

from __block.constants import BLOCK_TYPE
from __data.assertions import assert_object_data_is_correct
from notion_api.data.blocks import Block, BlockType
from __data.utils.__serialization import remove_none_values, remove_children_keys


def assert_block_data_is_correct(data: Block, expected_block_type: BlockType):
    assert_object_data_is_correct(data, "block")
    assert data.has_children is False
    assert data.children == []
    assert data.type == expected_block_type


T = TypeVar("T", bound=Block)


def create_block_structure(block_class: Type[T], data_provider: Callable) -> T:
    block_type = block_class.get_associated_block_type()

    block_data = data_provider(block_type)
    block = block_class(**block_data)

    assert block.__class__ == block_class
    return block


def assert_serialization_to_json(block, block_type_specific_data):
    block_data = remove_none_values(block_type_specific_data)
    block_data = remove_children_keys(block_data)
    json = block.serialize_to_json()
    assert json["object"] == BLOCK_TYPE
    property_name = block.__class__.get_payload_property_name()
    assert json["type"] == property_name
    print(json[property_name])
    print(block_data)
    assert json[property_name] == block_data
