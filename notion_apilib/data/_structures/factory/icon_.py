# icon_factory.py

# Standard Library

from ..data import Emoji


def create_emoji(emoji: str, type_: str) -> Emoji:
    """
    Factory method to create an Emoji.

    Parameters
    ----------
    emoji : str
        The emoji character.
    type_ : str
        The type of the emoji.

    Returns
    -------
    Emoji
        A new Emoji instance.
    """
    return Emoji(emoji=emoji, type=type_)


__all__ = ["create_emoji"]
