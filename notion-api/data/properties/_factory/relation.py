from datetime import datetime
from typing import Optional, Literal, Any
from uuid import UUID

from Page import Page
from PropertyType import PropertyType
from RelationProperty import RelationPage, RelationStructure, RollupPage, RollupStructure
from factory.general import _create_page_property


def create_relation_page(
        parent: Page, name: str, relation_ids: list[UUID], id_: Optional[str] = None) -> RelationPage:
    """
    Factory method to create a RelationPage object.

    Parameters:
        parent (Page): The parent page to which this relation property belongs.
        name (str): The name of the relation property.
        relation_ids (list[UUID]): A list of UUIDs for the related items.
        id_ (Optional[str]): The optional ID of the relation property.

    Returns:
        RelationPage: A new RelationPage object.
    """
    relations = [RelationStructure(id=rid) for rid in relation_ids]
    return _create_page_property(
        RelationPage,
        parent=parent,
        property_type=PropertyType.RELATION,
        name=name,
        id_=id_,
        relation=relations
    )


def create_rollup_page(
        parent: Page, name: str, type: Literal['array', 'date', 'number', 'incomplete', 'unsupported'],
        function: str, array: Optional[list[Any]] = None, date: Optional[datetime] = None,
        number: Optional[float] = None, incomplete: Optional[Any] = None,
        unsupported: Optional[Any] = None, id_: Optional[str] = None) -> RollupPage:
    """
    Factory method to create a RollupPage object.

    Parameters:
        parent (Page): The parent page to which this rollup property belongs.
        name (str): The name of the rollup property.
        type (Literal['array', 'date', 'number', 'incomplete', 'unsupported']): The type of the rollup.
        function (str): The function of the rollup.
        array (Optional[list[Any]]): The optional array value of the rollup.
        date (Optional[datetime]): The optional date value of the rollup.
        number (Optional[float]): The optional number value of the rollup.
        incomplete (Optional[Any]): The optional incomplete value of the rollup.
        unsupported (Optional[Any]): The optional unsupported value of the rollup.
        id_ (Optional[str]): The optional ID of the rollup property.

    Returns:
        RollupPage: A new RollupPage object.
    """
    return _create_page_property(
        RollupPage,
        parent=parent,
        property_type=PropertyType.ROLLUP,
        name=name,
        id_=id_,
        rollup=RollupStructure(
            type=type, function=function, array=array, date=date,
            number=number, incomplete=incomplete, unsupported=unsupported)
    )
