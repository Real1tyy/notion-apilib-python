# Standard Library
from datetime import datetime
from typing import Any, Literal, Optional
from uuid import UUID

# Third Party
from pydantic import BaseModel, Field

# First Party
from notion_api.data._properties.property import DatabaseProperty, PageProperty
from notion_api.data._properties.type_ import PropertyType


class RelationStructure(BaseModel):
    """
    A model representing a structure for a relation property.

    Attributes:
        id (UUID): The UUID of the related item.
    """
    id: UUID


class RelationPage(PageProperty):
    """
    A model representing a relation property for a page.

    Attributes:
        has_more (bool): Indicates if there are more relations.
        relation (list[RelationStructure]): A list of relation _structures.
    """
    has_more: bool = Field(exclude=True)
    relation: list[RelationStructure]

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.RELATION


class DualProperty(BaseModel):
    """
    A model representing a dual property for a relation database property.

    Attributes:
        synced_property_id (str): The ID of the synced property.
        synced_property_name (str): The name of the synced property.
    """
    synced_property_id: str
    synced_property_name: str


class SingleProperty(BaseModel, extra='allow'):
    """
    A model representing a single property for a relation database property.
    """
    pass


class RelationDatabaseStructure(BaseModel):
    """
    A model representing the structure for a relation property in a database.

    Attributes:
        database_id (UUID): The UUID of the related database.
        dual_property (Optional[DualProperty]): The optional dual property structure.
        single_property (Optional[SingleProperty]): The optional single property structure.
    """
    database_id: UUID
    type: Literal['dual_property', 'single_property']
    dual_property: Optional[DualProperty] = None
    single_property: Optional[SingleProperty] = None


class RelationDatabase(DatabaseProperty):
    """
    A model representing a relation property for a database.

    Attributes:
        relation (RelationDatabaseStructure): The relation structure of the database property.
    """
    relation: RelationDatabaseStructure

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.RELATION


class RollupStructure(BaseModel):
    """
    A model representing the structure for a rollup property.

    Attributes:
        type (Literal['array', 'date', 'number', 'incomplete', 'unsupported']): The type of the rollup.
        function (str): The function of the rollup.
        array (Optional[list[Any]]): The optional array value of the rollup.
        date (Optional[datetime]): The optional date value of the rollup.
        number (Optional[float]): The optional number value of the rollup.
        incomplete (Optional[Any]): The optional incomplete value of the rollup.
        unsupported (Optional[Any]): The optional unsupported value of the rollup.
    """
    type: Literal['array', 'date', 'number', 'incomplete', 'unsupported']
    function: str
    array: Optional[list[Any]] = None
    date: Optional[datetime] = None
    number: Optional[float] = None
    incomplete: Optional[Any] = None
    unsupported: Optional[Any] = None


class RollupPage(PageProperty):
    """
    A model representing a rollup property for a page.

    Attributes:
        rollup (RollupStructure): The rollup structure of the page property.
    """
    rollup: RollupStructure

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.ROLLUP


class RollupDatabaseStructure(BaseModel):
    """
    A model representing the structure for a rollup property in a database.

    Attributes:
        relation_property_id (str): The ID of the related property.
        relation_property_name (str): The name of the related property.
        rollup_property_name (str): The name of the rollup property.
        rollup_property_id (str): The ID of the rollup property.
        function (str): The function of the rollup.
    """
    relation_property_id: str
    relation_property_name: str
    rollup_property_name: str
    rollup_property_id: str
    function: str


class RollupDatabase(DatabaseProperty):
    """
    A model representing a rollup property for a database.

    Attributes:
        rollup (RollupDatabaseStructure): The rollup structure of the database property.
    """
    rollup: RollupDatabaseStructure

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.ROLLUP


__all__ = [
    'RelationPage', 'RelationDatabase',
    'RollupPage', 'RollupDatabase']
