# Standard Library
from abc import ABC
from typing import Type

from pydantic import Field

# Third Party
from BlockType import BlockType
from Parent import Parent
from object import Object


class Block(Object, ABC):
    type: BlockType
    has_children: bool
    children: list['Block'] = Field(default=[], exclude=True)

    def deserialize_json(self):
        return self.model_dump(
            mode='json', exclude_none=True,
            exclude={'id', 'parent', 'archived', 'in_trash'})


def _create_block(cls: Type, parent: Parent, block_type: BlockType, children: list['Block'] = None, **kwargs):
    """
       Helper function to create block objects with common parameters pre-filled.
       :param cls: The class of the block object to create
       :param parent: The parent object
       :param block_type: The type of the block
       :param children: The list of children blocks, if any, otherwise by default None
       :param kwargs: Additional keyword arguments specific to the block type
       :return: A new block object of the specified class
   """
    common_params = {
        "object": "block",
        "archived": False,
        "in_trash": False,
        "parent": parent,
        "type": block_type,
        "has_children": bool(children),
        "children": children if children else []
    }
    return cls(**common_params, **kwargs)
