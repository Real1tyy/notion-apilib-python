import datetime
from abc import ABC
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

from Emoji import Icon
from Parent import Parent


class Object(ABC, BaseModel, use_enum_values=True, from_attributes=True, arbitrary_types_allowed=True):
    id: UUID = Field(default=None)
    object: str
    created_time: datetime.datetime = Field(exclude=True, default=None)
    last_edited_time: datetime.datetime = Field(exclude=True, default=None)
    parent: Parent
    archived: bool
    in_trash: bool


class MajorObject(Object, ABC):
    icon: Icon
    cover: Optional[str] = None
    url: Optional[str] = None
    public_url: Optional[str] = None
