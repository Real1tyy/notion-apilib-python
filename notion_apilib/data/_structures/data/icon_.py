# Standard Library

# Third Party
from pydantic import BaseModel

# First Party


class Emoji(BaseModel):
    """
    Represents an Emoji in the Notion API.

    Attributes
    ----------
    emoji : str
        The emoji character.
    type : str
        The type of the emoji.
    """

    emoji: str
    type: str


__all__ = ["Emoji"]
