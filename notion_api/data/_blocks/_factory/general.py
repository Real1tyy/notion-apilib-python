from typing import Type, TypeVar, Any, Optional

from notion_api.data.structures import Parent
from notion_api.data._blocks.block import Block

T = TypeVar('T', bound=Block)


def _create_block(
        cls: Type[T], parent: Parent, block_type_specific_params: Optional[Any] = None, children: list[
            Block] = None) \
        -> T:
    """
    Helper function to create block objects with common parameters pre-filled.

    :param cls: The class of the block object to create.
    :type cls: Type[T]
    :param parent: The parent object.
    :type parent: Parent
    :param block_type_specific_params: The parameters specific to the block type.
    :type block_type_specific_params: Any
    :param children: The list of children blocks, if any. Defaults to None.
    :type children: list[Block], optional
    :return: A new block object of the specified class.
    :rtype: T
    """
    common_params = {
        "object": "block",
        "archived": False,
        "in_trash": False,
        "parent": parent,
        "type": cls.get_associated_block_type(),
        "has_children": bool(children),
        "children": children if children else []
    }
    if block_type_specific_params:
        payload_property_name = cls.get_payload_property_name()
        common_params[payload_property_name] = block_type_specific_params
    return cls(**common_params)
