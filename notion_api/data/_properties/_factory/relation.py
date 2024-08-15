from datetime import datetime
from typing import Optional, Literal, Any
from uuid import UUID

from .general import _create_page_property, _create_database_property
from notion_api.data._properties._data.relation import (RelationPage, RelationStructure, RollupPage, RollupStructure,
                                                        RelationDatabase, \
                                                        RollupDatabase, RollupDatabaseStructure,
                                                        RelationDatabaseStructure)


def create_relation_page(
        parent: 'Page', name: str, relation_ids: list[UUID]) -> RelationPage:
    """
    Factory method to create a RelationPage object.

    Parameters:
        parent (Page): The parent page to which this relation property belongs.
        name (str): The name of the relation property.
        relation_ids (list[UUID]): A list of UUIDs for the related items.

    Returns:
        RelationPage: A new RelationPage object.
    """
    relations = [RelationStructure(id=id_) for id_ in relation_ids]
    return _create_page_property(
        RelationPage,
        parent=parent,
        name=name,
        property_specific_params=relations
    )


def create_relation_database(
        parent: 'Database', name: str, database_id: UUID,
        synced_property_id: Optional[str] = None,
        synced_property_name: Optional[str] = None) -> RelationDatabase:
    """
    Factory method to create a RelationDatabase object.

    Parameters:
        parent (Database): The parent database to which this relation property belongs.
        name (str): The name of the relation property.
        database_id (UUID): The UUID of the related database.
        synced_property_id (Optional[str]): The optional ID of the synced property.
        synced_property_name (Optional[str]): The optional name of the synced property.

    Returns:
        RelationDatabase: A new RelationDatabase object.
    """
    dual_property = None
    single_property = None

    if synced_property_id and synced_property_name:
        dual_property = {
            "synced_property_id": synced_property_id,
            "synced_property_name": synced_property_name
        }
    else:
        single_property = {}

    return _create_database_property(
        RelationDatabase,
        parent=parent,
        name=name,
        property_specific_params=RelationDatabaseStructure(
            database_id=database_id,
            dual_property=dual_property,
            single_property=single_property
        )
    )


def create_rollup_page(
        parent: 'Page', name: str, type_: Literal['array', 'date', 'number', 'incomplete', 'unsupported'],
        function: str, array: Optional[list[Any]] = None, date: Optional[datetime] = None,
        number: Optional[float] = None, incomplete: Optional[Any] = None,
        unsupported: Optional[Any] = None) -> RollupPage:
    """
    Factory method to create a RollupPage object.

    Parameters:
        parent (Page): The parent page to which this rollup property belongs.
        name (str): The name of the rollup property.
        type_ (Literal['array', 'date', 'number', 'incomplete', 'unsupported']): The type of the rollup.
        function (str): The function of the rollup.
        array (Optional[list[Any]]): The optional array value of the rollup.
        date (Optional[datetime]): The optional date value of the rollup.
        number (Optional[float]): The optional number value of the rollup.
        incomplete (Optional[Any]): The optional incomplete value of the rollup.
        unsupported (Optional[Any]): The optional unsupported value of the rollup.

    Returns:
        RollupPage: A new RollupPage object.
    """
    return _create_page_property(
        RollupPage,
        parent=parent,
        name=name,
        property_specific_params=RollupStructure(
            type=type_, function=function, array=array, date=date,
            number=number, incomplete=incomplete, unsupported=unsupported)
    )


def create_rollup_database(
        parent: 'Database', name: str, relation_property_id: str, relation_property_name: str,
        rollup_property_name: str, rollup_property_id: str, function: str) -> RollupDatabase:
    """
    Factory method to create a RollupDatabase object.

    Parameters:
        parent (Database): The parent database to which this rollup property belongs.
        name (str): The name of the rollup property.
        relation_property_id (str): The ID of the related property.
        relation_property_name (str): The name of the related property.
        rollup_property_name (str): The name of the rollup property.
        rollup_property_id (str): The ID of the rollup property.
        function (str): The function of the rollup.

    Returns:
        RollupDatabase: A new RollupDatabase object.
    """
    return _create_database_property(
        RollupDatabase,
        parent=parent,
        name=name,
        property_specific_params=RollupDatabaseStructure(
            relation_property_id=relation_property_id,
            relation_property_name=relation_property_name,
            rollup_property_name=rollup_property_name,
            rollup_property_id=rollup_property_id,
            function=function
        )
    )


__all__ = ['create_relation_page', 'create_relation_database', 'create_rollup_page', 'create_rollup_database']
