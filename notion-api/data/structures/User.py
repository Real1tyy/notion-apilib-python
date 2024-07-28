from typing import Annotated, Literal
from uuid import UUID

from pydantic import BaseModel
from pydantic.types import UuidVersion


class UserStructure(BaseModel):
    object: Literal['user']
    id: Annotated[UUID, UuidVersion(4)]
