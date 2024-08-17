# Standard Library
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Literal, Optional
from uuid import UUID

# Third Party
from pydantic import Field

# First Party
from notion_apilib.data.structures import Parent, ResourcesAttributes, User

from .configuration_ import BasicConfiguration
from .properties import Property


class Object(BasicConfiguration, ABC):
    id: UUID = Field(default=None)
    object: Literal["block", "database", "page", "workspace"]
    created_time: datetime = Field(exclude=True)
    last_edited_time: datetime = Field(exclude=True)
    created_by: User = Field(exclude=True)
    last_edited_by: User = Field(exclude=True)
    parent: Parent
    archived: bool
    in_trash: bool

    @abstractmethod
    def serialize_to_json(self) -> dict:
        """
        Serialize the object to a JSON dictionary
        :return: The serialized object
        """


class MajorObject(Object, ABC):
    icon: Optional[ResourcesAttributes] = None
    cover: Optional[ResourcesAttributes] = None
    url: str
    public_url: Optional[str] = None

    @property
    @abstractmethod
    def properties(self) -> list[Property]:
        """
        Get the properties of the object.
        :return:
        """

    @abstractmethod
    def add_property(self, property_: Property) -> None:
        """
        Add a property to the object properties.
        :param property_: Property to add.
        :return:
        """
