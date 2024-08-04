# Standard Library
from typing import Any, Literal, Optional
from uuid import UUID

# Third Party
from pydantic import BaseModel

parents_types = Literal['database_id', 'page_id', 'block_id', 'workspace']


class Parent(BaseModel):
    type: parents_types
    database_id: Optional[UUID] = None
    page_id: Optional[UUID] = None
    workspace: Optional[Literal[True]] = None
    block_id: Optional[UUID] = None

    def get_parent_id(self) -> str:
        """
        Get the parent id of the parent object
        :return: id of the parent object or 'workspace' if the parent is the root object
        """
        if self.database_id:
            return self.database_id.hex
        if self.page_id:
            return self.page_id.hex
        if self.block_id:
            return self.block_id.hex
        return "workspace"

    def set_parent_id(self, parent_type: parents_types, parent_id: Optional[UUID] = None):
        """
        Sets the parent id of the parent object
        """
        self.remove_ids()
        match parent_type:
            case "block_id":
                self.block_id = parent_id
            case "page_id":
                self.page_id = parent_id
            case "database_id":
                self.database_id = parent_id
            case _:
                self.workspace = True

    def remove_ids(self):
        self.database_id = None
        self.page_id = None
        self.block_id = None


def create_parent_from_object(parent: Any) -> Parent:
    """
    Creates the parent of the object, parent parameter should be subtype of Object class
    """
    parent_type: Literal['page_id', 'block_id', 'database_id']
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
    Creates the parent of the object
    """
    parent = Parent(type=parent_type)
    if parent_id:
        parent.set_parent_id(parent_type, UUID(parent_id))
    return parent
