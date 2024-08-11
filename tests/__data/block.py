from functools import wraps
from typing import Any, Callable, Dict, Type, TypeVar

from notion_api.data.blocks import Block, BlockType
from __data.object import _create_major_object_data, assert_object_data_is_correct


def _create_block_data(block_type: BlockType) -> dict[str, Any]:
    data = _create_major_object_data("block")
    block_data = {
        "has_children": False,
        "type": block_type,
    }
    data.update(block_data)
    return data


def add_block_data(block_type: BlockType) -> Callable:
    """
    Decorator to block object data to the dictionary returned by the decorated
    function.

    Args:
        block_type (BlockType): The type of the block object to be added.

    Returns:
        Callable: A decorated function that returns a dictionary extended with block data.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Dict[str, Any]:
            data = func(*args, **kwargs)
            block_data = _create_block_data(block_type)
            block_data[block_type.value] = data
            return block_data

        return wrapper

    return decorator


T = TypeVar("T", bound=Block)


def create_block_structure(block_class: Type[T], data_provider: Callable) -> T:
    block_type = block_class.get_associated_block_type()

    block_data = data_provider(block_type)
    block = block_class(**block_data)

    assert block.__class__ == block_class
    return block


def assert_block_data_is_correct(data: Block, expected_block_type: BlockType):
    assert_object_data_is_correct(data, "block")
    assert data.has_children is False
    assert data.children == []
    assert data.type == expected_block_type
