# Standard Library
from typing import Any, Literal
from uuid import UUID

# First Party
from ..data import Parent
from ..types_ import parents_types


def create_parent_from_object(parent: Any) -> Parent:
    """
    Creates a Parent object from an existing object.

    Parameters
    ----------
    parent : Any
        The parent parameter should be a subtype of the Object class.

    Returns
    -------
    Parent
        A new Parent instance.
    """
    parent_type: Literal["page_id", "block_id", "database_id"]
    match parent.object:
        case "_blocks":
            parent_type = "block_id"
        case "database":
            parent_type = "database_id"
        case _:
            parent_type = "page_id"

    result_parent = Parent(type=parent_type)
    result_parent.set_parent_id(parent_type, UUID(parent.id))
    return result_parent


def create_parent(parent_type: parents_types, parent_id: str = None) -> Parent:
    """
    Creates a Parent object.

    Parameters
    ----------
    parent_type : parents_types
        The type of the parent object.
    parent_id : str, optional
        The UUID of the parent object, if any.

    Returns
    -------
    Parent
        A new Parent instance.
    """
    parent = Parent(type=parent_type)
    if parent_id:
        parent.set_parent_id(parent_type, UUID(parent_id))
    return parent


__all__ = ["create_parent_from_object", "create_parent"]
