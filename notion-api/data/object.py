# Standard Library
from datetime import datetime
from abc import ABC
from typing import Literal, Optional
from uuid import UUID

from pydantic import BaseModel, Field
from data.structures import Icon, Parent


# Third Party


class Object(ABC, BaseModel, use_enum_values=True, from_attributes=True, arbitrary_types_allowed=True):
    id: UUID = Field(default=None)
    object: Literal['blocks', 'database', 'page', 'user', 'workspace']
    created_time: datetime = Field(exclude=True, default=None)
    last_edited_time: datetime = Field(exclude=True, default=None)
    parent: Parent
    archived: bool
    in_trash: bool


class MajorObject(Object, ABC):
    icon: Optional[Icon] = None
    cover: Optional[str] = None
    url: Optional[str] = None
    public_url: Optional[str] = None
