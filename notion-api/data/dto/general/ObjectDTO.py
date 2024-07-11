import datetime
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, BeforeValidator
from pydantic.types import UuidVersion

from validators import parent_validator


class ObjectDTO(BaseModel):
    model_config: ConfigDict = ConfigDict(from_attributes=True)

    id: Annotated[UUID, UuidVersion(4)]
    object: str

    created_time: datetime.datetime
    last_edited_time: datetime.datetime

    parent: Annotated[UUID, UuidVersion(4), BeforeValidator(parent_validator)]
    archived: bool
    in_trash: bool
