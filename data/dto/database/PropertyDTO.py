from typing import Optional, Any, Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict
from pydantic.types import UuidVersion

from database.PropertyTypes import PropertyTypes


class RelationDetails(BaseModel):
    model_config: ConfigDict = ConfigDict(from_attributes=True)
    database_id: str
    type: str
    dual_property: Optional[dict[str, str]] = None
    single_property: Optional[dict[str, str]] = None


class PropertyDTO(BaseModel):
    model_config: ConfigDict = ConfigDict(from_attributes=True)

    id: Annotated[UUID, UuidVersion(4)]
    name: str
    type: PropertyTypes

    relation: Optional[RelationDetails] = None
    unique_id: Optional[dict[str, Any]] = None
    rollup: Optional[dict[str, Any]] = None
    last_edited_time: Optional[dict[str, Any]] = None
    created_time: Optional[dict[str, Any]] = None
    checkbox: Optional[dict[str, Any]] = None
    rich_text: Optional[dict[str, Any]] = None
    select: Optional[dict[str, Any]] = None
    status: Optional[dict[str, Any]] = None
    title: Optional[dict[str, Any]] = None
