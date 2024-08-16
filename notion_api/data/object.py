# Standard Library
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Literal, Optional
from uuid import UUID

# Third Party
from pydantic import Field

# First Party
from notion_api.data.configuration import BasicConfiguration
from notion_api.data.structures import Icon, Parent, User


class Object(BasicConfiguration, ABC):
    id: UUID = Field(default=None)
    object: Literal['block', 'database', 'page', 'workspace']
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
    url: str
    public_url: Optional[str] = None

    @abstractmethod
    def get_properties(self):
        pass

    @abstractmethod
    def add_property(self, property_):
        pass
