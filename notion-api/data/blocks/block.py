# Standard Library
from abc import ABC
from typing import Type

from pydantic import Field

from Parent import Parent
from object import Object
# Third Party
from type import BlockType


class Block(Object, ABC):
    """
    Represents a Block in the Notion API.

    Attributes
    ----------
    type : BlockType
        The type of the block.
    has_children : bool
        Whether the block has children.
    children : list[Block]
        The list of children blocks.
    """
    type: BlockType
    has_children: bool
    children: list['Block'] = Field(default=[], exclude=True)

    def deserialize_json(self):
        """
        Deserialize the block to JSON format, excluding certain fields.

        :return: The JSON representation of the block.
        :rtype: dict
        """
        return self.model_dump(
            mode='json', exclude_none=True,
            exclude={'id', 'parent', 'archived', 'in_trash'}
        )


def _create_block(cls: Type, parent: Parent, block_type: BlockType, children: list['Block'] = None, **kwargs):
    """
       Helper function to create blocks objects with common parameters pre-filled.
       :param cls: The class of the blocks object to create
       :param parent: The parent object
       :param block_type: The type of the blocks
       :param children: The list of children blocks, if any, otherwise by default None
       :param kwargs: Additional keyword arguments specific to the blocks type
       :return: A new blocks object of the specified class
   """
    common_params = {
        "object": "blocks",
        "archived": False,
        "in_trash": False,
        "parent": parent,
        "type": block_type,
        "has_children": bool(children),
        "children": children if children else []
    }
    return cls(**common_params, **kwargs)
