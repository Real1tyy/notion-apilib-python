# user_factory.py

from typing import Optional, Literal
from uuid import UUID

from notion_api.data._structures.data import User, PeopleStructure, People, OwnerStructure, BotStructure, Bot


def create_user(
        object_: Literal['user'], id_: UUID, type_: Optional[Literal['person', 'bot']] = None,
        name: Optional[str] = None, avatar_url: Optional[str] = None
) -> User:
    """
    Factory method to create a User.

    Parameters
    ----------
    object_ : Literal['user']
        The type of the object, always 'user'.
    id_ : UUID
        The unique identifier of the user.
    type_ : Optional[Literal['person', 'bot']]
        The type of the user, either 'person' or 'bot'. Defaults to None.
    name : Optional[str]
        The name of the user. Defaults to None.
    avatar_url : Optional[str]
        The URL of the user's avatar. Defaults to None.

    Returns
    -------
    User
        A new User instance.
    """
    return User(object=object_, id=id_, type=type_, name=name, avatar_url=avatar_url)


def create_people_structure(email: str) -> PeopleStructure:
    """
    Factory method to create a PeopleStructure.

    Parameters
    ----------
    email : str
        The email of the person.

    Returns
    -------
    PeopleStructure
        A new PeopleStructure instance.
    """
    return PeopleStructure(email=email)


def create_people(
        object_: Literal['user'], id_: UUID, person: PeopleStructure, type_: Optional[Literal['person']] = 'person',
        name: Optional[str] = None, avatar_url: Optional[str] = None
) -> People:
    """
    Factory method to create a People instance.

    Parameters
    ----------
    object_ : Literal['user']
        The type of the object, always 'user'.
    id_ : UUID
        The unique identifier of the user.
    person : PeopleStructure
        The person structure containing additional details.
    type_ : Optional[Literal['person']]
        The type of the user, always 'person'. Defaults to 'person'.
    name : Optional[str]
        The name of the user. Defaults to None.
    avatar_url : Optional[str]
        The URL of the user's avatar. Defaults to None.

    Returns
    -------
    People
        A new People instance.
    """
    return People(object=object_, id=id_, type=type_, name=name, avatar_url=avatar_url, person=person)


def create_owner_structure(type_: Literal['user', 'workspace']) -> OwnerStructure:
    """
    Factory method to create an OwnerStructure.

    Parameters
    ----------
    type_ : Literal['user', 'workspace']
        The type of the owner, either 'user' or 'workspace'.

    Returns
    -------
    OwnerStructure
        A new OwnerStructure instance.
    """
    return OwnerStructure(type=type_)


def create_bot_structure(owner: OwnerStructure, workspace_name: str) -> BotStructure:
    """
    Factory method to create a BotStructure.

    Parameters
    ----------
    owner : OwnerStructure
        The owner structure of the bot.
    workspace_name : str
        The name of the workspace the bot belongs to.

    Returns
    -------
    BotStructure
        A new BotStructure instance.
    """
    return BotStructure(owner=owner, workspace_name=workspace_name)


def create_bot(
        object_: Literal['user'], id_: UUID, bot: BotStructure, type_: Optional[Literal['bot']] = 'bot',
        name: Optional[str] = None, avatar_url: Optional[str] = None
) -> Bot:
    """
    Factory method to create a Bot instance.

    Parameters
    ----------
    object_ : Literal['user']
        The type of the object, always 'user'.
    id_ : UUID
        The unique identifier of the user.
    bot : BotStructure
        The bot structure containing additional details.
    type_ : Optional[Literal['bot']]
        The type of the user, always 'bot'. Defaults to 'bot'.
    name : Optional[str]
        The name of the user. Defaults to None.
    avatar_url : Optional[str]
        The URL of the user's avatar. Defaults to None.

    Returns
    -------
    Bot
        A new Bot instance.
    """
    return Bot(object=object_, id=id_, type=type_, name=name, avatar_url=avatar_url, bot=bot)


__all__ = ['create_user', 'create_people_structure', 'create_people', 'create_owner_structure', 'create_bot_structure',
           'create_bot']
