from typing import Optional, Annotated, Literal
from uuid import UUID

from pydantic import BaseModel
from pydantic.types import UuidVersion


class Parent(BaseModel):
    type: str
    database_id: Optional[Annotated[UUID, UuidVersion(4)]] = None
    page_id: Optional[Annotated[UUID, UuidVersion(4)]] = None
    workspace: Optional[Literal[True]] = None
    block_id: Optional[Annotated[UUID, UuidVersion(4)]] = None
