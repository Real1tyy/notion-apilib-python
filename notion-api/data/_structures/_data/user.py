# Standard Library
from typing import Literal, Optional
from uuid import UUID

# Third Party
from pydantic import BaseModel


class User(BaseModel):
    object: Literal['user']
    id: UUID
    type: Optional[Literal['person', 'bot']] = None
    name: Optional[str] = None
    avatar_url: Optional[str] = None


class PeopleStructure(BaseModel):
    email: str


class People(User):
    person: PeopleStructure


class OwnerStructure(BaseModel):
    type: Literal['user', 'workspace']


class BotStructure(BaseModel):
    owner: OwnerStructure
    workspace_name: str


class Bot(User):
    bot: BotStructure
