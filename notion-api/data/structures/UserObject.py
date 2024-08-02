from typing import Literal, Optional
from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    object: Literal['user']
    id: UUID
    type: Optional[Literal['person', 'bot']] = None
    name: Optional[str] = None
    avatar_url: Optional[str] = None
