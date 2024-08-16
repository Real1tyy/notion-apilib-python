# Standard Library
from typing import Literal

from .general_ import Filter, FilterStructure


class RelationFilter(Filter):
    """
    A filter class for applying a relation-based filter to a Notion database query.

    Attributes:
        property (str): The name of the property to apply the filter to.
        relation (FilterStructure): The filter criteria for the relation property.
    """

    relation: FilterStructure


def create_relation_filter_contains(
    property_name: str, contains: str
) -> RelationFilter:
    """
    Factory function to create a RelationFilter object that checks if the relation property contains a specific UUID.

    Args:
        property_name (str): The name of the property to apply the relation filter to.
        contains (str): The UUID to check if the relation property contains.

    Returns:
        RelationFilter: The constructed RelationFilter object with the specified property and filter criteria.
    """
    return RelationFilter(
        property=property_name, relation=FilterStructure(contains=contains)
    )


def create_relation_filter_does_not_contain(
    property_name: str, does_not_contain: str
) -> RelationFilter:
    """
    Factory function to create a RelationFilter object that checks if the relation property does not contain a specific UUID.

    Args:
        property_name (str): The name of the property to apply the relation filter to.
        does_not_contain (str): The UUID to check if the relation property does not contain.

    Returns:
        RelationFilter: The constructed RelationFilter object with the specified property and filter criteria.
    """
    return RelationFilter(
        property=property_name,
        relation=FilterStructure(does_not_contain=does_not_contain),
    )


def create_relation_filter_is_empty(
    property_name: str, is_empty: bool
) -> RelationFilter:
    """
    Factory function to create a RelationFilter object that checks if the relation property is empty or not.

    Args:
        property_name (str): The name of the property to apply the relation filter to.
        is_empty (bool): Whether to check if the relation property is empty or not.

    Returns:
        RelationFilter: The constructed RelationFilter object with the specified property and filter criteria.
    """
    if is_empty:
        return RelationFilter(
            property=property_name, relation=FilterStructure(is_empty=True)
        )
    return RelationFilter(
        property=property_name, relation=FilterStructure(is_not_empty=True)
    )


class RollupFilter(Filter):
    """
    A filter class for applying a rollup-based filter to a Notion database query.

    Attributes:
        property (str): The name of the property to apply the filter to.
        rollup (FilterStructure): The filter criteria for the rollup property.
    """

    rollup: FilterStructure


def create_rollup_filter(
    property_name: str, filter_type: Literal["any", "every", "none"], criteria: Filter
) -> RollupFilter:
    """
    Factory function to create a RollupFilter object for array rollup values.

    Args:
        property_name (str): The name of the property to apply the rollup filter to.
        filter_type (Literal): The type of array rollup filter to apply ('any', 'every', 'none').
        criteria (Dict[str, FilterStructure]): The filter criteria for each item in the rollup array.

    Returns:
        RollupFilter: The constructed RollupFilter object with the specified property and filter criteria.
    """
    first_filter = FilterStructure()
    data = criteria.serialize_to_json()
    data.pop("property")
    setattr(first_filter, filter_type, data)
    return RollupFilter(property=property_name, rollup=first_filter)


__all__ = [
    "RelationFilter",
    "create_relation_filter_contains",
    "create_relation_filter_does_not_contain",
    "create_relation_filter_is_empty",
    "RollupFilter",
    "create_rollup_filter",
]
