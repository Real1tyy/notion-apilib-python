# icon_factory.py

from typing import Optional

from _structures.data import External, FileObject, Emoji, Icon
from types_ import file_type


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


def create_icon(type_: file_type, external: Optional[External] = None, file: Optional[FileObject] = None) -> Icon:
    """
    Factory method to create an Icon.

    Parameters
    ----------
    type_ : file_type
        The type of the icon, either 'external' or 'file'.
    external : Optional[External]
        The external file object, if any. Defaults to None.
    file : Optional[FileObject]
        The file object, if any. Defaults to None.

    Returns
    -------
    Icon
        A new Icon instance.
    """
    return Icon(type=type_, external=external, file=file)


__all__ = ['create_emoji', 'create_icon']
