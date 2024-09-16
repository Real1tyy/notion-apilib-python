# Standard Library
from typing import Any, Literal, Optional
from uuid import UUID

# Third Party
from pydantic import BaseModel, model_validator

from ..._util import check_if_exactly_one_not_none_val
from ..types_ import parents_types


class Parent(BaseModel):
    """
    Represents a parent object in the Notion API.

    Attributes
    ----------
    type : parents_types
        The type of the parent object, either 'database_id', 'page_id', 'block_id', or 'workspace'.
    database_id : Optional[UUID]
        The UUID of the parent database, if any.
    page_id : Optional[UUID]
        The UUID of the parent page, if any.
    workspace : Optional[Literal[True]]
        Indicates if the parent is the workspace root object.
    block_id : Optional[UUID]
        The UUID of the parent block, if any.
    """

    type: parents_types
    database_id: Optional[UUID] = None
    page_id: Optional[UUID] = None
    workspace: Optional[Literal[True]] = None
    block_id: Optional[UUID] = None

    @classmethod
    @model_validator(mode="after")
    def parse_properties(cls, v: Any):
        properties = [v.database_id, v.page_id, v.block_id, v.workspace]
        if check_if_exactly_one_not_none_val(properties):
            raise ValueError(f"Only one of the values from: {properties} can be provided.")
        return v

    def get_parent_id(self) -> str:
        """
        Get the parent id of the parent object.

        Returns
        -------
        str
            The id of the parent object or 'workspace' if the parent is the root object.
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
        Sets the parent id of the parent object.

        Parameters
        ----------
        parent_type : parents_types
            The type of the parent object.
        parent_id : Optional[UUID]
            The UUID of the parent object, if any.
        """
        self.reset_values()
        match parent_type:
            case "block_id":
                self.block_id = parent_id
            case "page_id":
                self.page_id = parent_id
            case "database_id":
                self.database_id = parent_id
            case _:
                self.workspace = True

    def reset_values(self):
        """
        Removes all parent ids.
        """
        self.database_id = None
        self.page_id = None
        self.block_id = None
        self.workspace = None


__all__ = ["Parent"]
