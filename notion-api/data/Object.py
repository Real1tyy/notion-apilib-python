import datetime
from abc import ABC
from typing import Annotated, Optional
from uuid import UUID

from pydantic import BaseModel, BeforeValidator, Field
from pydantic.types import UuidVersion

from Parent import Parent
from validation.validators import icon_validator


class Object(ABC, BaseModel, use_enum_values=True, from_attributes=True, arbitrary_types_allowed=True):
    id: Annotated[UUID, UuidVersion(4)]
    object: str
    created_time: datetime.datetime = Field(exclude=True)
    last_edited_time: datetime.datetime = Field(exclude=True)
    parent: Parent
    archived: bool
    in_trash: bool


class MajorObject(Object, ABC):
    icon: Annotated[str, BeforeValidator(icon_validator)]
    cover: Optional[str] = None
    url: Optional[str] = None
    public_url: Optional[str] = None
