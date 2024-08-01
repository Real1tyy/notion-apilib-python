from typing import Optional, Literal
from uuid import UUID

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
        if self.database_id is not None:
            return self.database_id.hex

        if self.page_id is not None:
            return self.page_id.hex

        if self.block_id is not None:
            return self.block_id.hex

        return "workspace"


def create_parent_from_object(parent: parents_types) -> Parent:
    """
    Set the parent of the object, parent parameter should be subtype of Object class
    """
    if parent.object == "block_id":
        return Parent(type="block_id", block_id=parent.id)

    if parent.object == "page_id":
        return Parent(type="page_id", page_id=parent.id)

    if parent.object == "database_id":
        return Parent(type="database_id", database_id=parent.id)

    if parent.object == "workspace":
        return Parent(type="workspace")


def create_parent(parent_type: parents_types, parent_id: str = None) -> Parent:
    """
    Set the parent of the object, parent parameter should be subtype of Object class
    """
    result_id = UUID(parent_id)
    if parent_type == "block_id":
        return Parent(type="block_id", block_id=result_id)

    if parent_type == "page_id":
        return Parent(type="page_id", page_id=result_id)

    if parent_type == "database_id":
        return Parent(type="database_id", database_id=result_id)

    if parent_type == "workspace":
        return Parent(type="workspace")
