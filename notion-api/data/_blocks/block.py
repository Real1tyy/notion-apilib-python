# Standard Library
from abc import ABC
from typing import Type

from pydantic import Field

from data.object import Object
# Third Party
from type import BlockType
from data.structures import Parent


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


def _create_block(cls: Type, parent: Parent, block_type: BlockType, children: list[Block] = None, **kwargs):
    """
    Helper function to create block objects with common parameters pre-filled.

    :param cls: The class of the block object to create.
    :type cls: Type
    :param parent: The parent object.
    :type parent: Parent
    :param block_type: The type of the block.
    :type block_type: BlockType
    :param children: The list of children blocks, if any. Defaults to None.
    :type children: list[Block], optional
    :param kwargs: Additional keyword arguments specific to the block type.
    :return: A new block object of the specified class.
    :rtype: Block
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


Block.model_rebuild()
