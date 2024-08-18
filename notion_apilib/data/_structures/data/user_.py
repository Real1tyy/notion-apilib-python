# Standard Library
from typing import Literal, Optional
from uuid import UUID

# Third Party
from pydantic import BaseModel


class User(BaseModel):
    """
    Represents a user in the Notion API.

    Attributes
    ----------
    object : Literal['user']
        The type of the object, always 'user'.
    id : UUID
        The unique identifier of the user.
    type : Optional[Literal['person', 'bot']]
        The type of the user, either 'person' or 'bot'. Defaults to None.
    name : Optional[str]
        The name of the user. Defaults to None.
    avatar_url : Optional[str]
        The URL of the user's avatar. Defaults to None.
    """

    object: Literal["user"]
    id: UUID
    type: Optional[Literal["person", "bot"]] = None
    name: Optional[str] = None
    avatar_url: Optional[str] = None


class PeopleStructure(BaseModel):
    """
    Represents the structure of a person in the Notion API.

    Attributes
    ----------
    email : str
        The email of the person.
    """

    email: str


class People(User):
    """
    Represents a person user in the Notion API.

    Attributes
    ----------
    person : PeopleStructure
        The person structure containing additional details.
    """

    person: PeopleStructure


class OwnerStructure(BaseModel):
    """
    Represents the owner structure in the Notion API.

    Attributes
    ----------
    type : Literal['user', 'workspace']
        The type of the owner, either 'user' or 'workspace'.
    """

    type: Literal["user", "workspace"]


class BotStructure(BaseModel):
    """
    Represents the structure of a bot in the Notion API.

    Attributes
    ----------
    owner : OwnerStructure
        The owner structure of the bot.
    workspace_name : str
        The name of the workspace the bot belongs to.
    """

    owner: OwnerStructure
    workspace_name: str


class Bot(User):
    """
    Represents a bot user in the Notion API.

    Attributes
    ----------
    bot : BotStructure
        The bot structure containing additional details.
    """

    bot: BotStructure


__all__ = ["Bot", "User", "People", "PeopleStructure", "OwnerStructure", "BotStructure"]
