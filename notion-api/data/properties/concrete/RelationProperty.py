from datetime import datetime
from typing import Literal, Optional, Any
from uuid import UUID

from pydantic import BaseModel, Field

from Property import PageProperty, DatabaseProperty


class RelationStructure(BaseModel):
    id: UUID


class RelationPage(PageProperty):
    has_more: bool = Field(exclude=True)
    relation: list[RelationStructure]


class RelationDatabaseStructure(BaseModel):
    database_id: UUID
    synced_property_id: str
    synced_property_name: str


class RelationDatabase(DatabaseProperty):
    relation: RelationDatabaseStructure


class RollupStructure(BaseModel):
    type: Literal['array', 'date', 'number', 'incomplete', 'unsupported']
    function: str
    array: Optional[list[Any]] = None
    date: Optional[datetime] = None
    number: Optional[float] = None
    incomplete: Optional[Any] = None
    unsupported: Optional[Any] = None


class RollupPage(PageProperty):
    rollup: RollupStructure


class RollupDatabaseStructure(BaseModel):
    relation_property_id: str
    relation_property_name: str
    rollup_property_name: str
    rollup_property_id: str
    function: str


class RollupDatabase(DatabaseProperty):
    rollup: RollupStructure
