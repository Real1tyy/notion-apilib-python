# Standard Library
from abc import ABC, abstractmethod
from typing import Type, Any

from pydantic import Field

from data.object import Object
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

    def serialize_to_json(self) -> dict[str, Any]:
        """
        Converts the block into a JSON payload suitable for creating or updating a block in Notion.
        Certain fields are omitted in the JSON representation, such as:
            - id
            - parent
            - archived
            - in_trash

        :return: The JSON representation of the block.
        :rtype: dict
        """
        return self.model_dump(
            mode='json', exclude_none=True,
            exclude={'id', 'parent', 'archived', 'in_trash'}
        )

    @classmethod
    @abstractmethod
    def get_associated_block_type(cls) -> BlockType:
        """
        Retrieves the block type associated with this class.

        :return: The associated BlockType enum value.
        :rtype: BlockType
        """
        pass

    @classmethod
    def get_payload_property_name(cls) -> str:
        """
        Retrieves the property name of the block type as a string, which is used in the Notion JSON format.
        Utilizes the get_associated_block_type method to obtain the enum value and converts it to a string.

        :return: The property name of the block type as a string.
        :rtype: str
        """
        return cls.get_associated_block_type().value


Block.model_rebuild()
