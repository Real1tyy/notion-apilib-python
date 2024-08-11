# Standard Library
from datetime import datetime
from abc import ABC, abstractmethod
from typing import Literal, Optional, Any
from uuid import UUID

from pydantic import Field

from configuration import BasicConfiguration
from structures import Icon, Parent, User


# Third Party


class Object(BasicConfiguration, ABC):
    id: UUID = Field(default=None)
    object: Literal['block', 'database', 'page', 'user', 'workspace']
    created_time: datetime = Field(exclude=True, default=None)
    last_edited_time: datetime = Field(exclude=True, default=None)
    created_by: User = Field(exclude=True)
    last_edited_by: User = Field(exclude=True)
    parent: Parent
    archived: bool
    in_trash: bool

    @abstractmethod
    def serialize_to_json(self) -> dict[str, Any]:
        pass


class MajorObject(Object, ABC):
    icon: Optional[Icon] = None
    cover: Optional[str] = None
    url: Optional[str] = None
    public_url: Optional[str] = None

    @abstractmethod
    def get_properties(self):
        pass

    @abstractmethod
    def add_property(self, property_):
        pass
