import datetime
from abc import ABC
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, BeforeValidator
from pydantic.types import UuidVersion

from validation.validators import parent_validator


class Object(ABC, BaseModel, use_enum_values=True, from_attributes=True):
    id: Annotated[UUID, UuidVersion(4)]
    object: str

    created_time: datetime.datetime
    last_edited_time: datetime.datetime

    parent: Annotated[str, BeforeValidator(parent_validator)]
    archived: bool
    in_trash: bool
