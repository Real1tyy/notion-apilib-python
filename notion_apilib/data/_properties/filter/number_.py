# Standard Library
from typing import Literal

from ._general import Filter, FilterStructure


class NumberFilter(Filter):
    """
    This class represents a filter for number properties in a database query.
    The filter is applied based on the structure provided in the `number` field.
    """

    number: FilterStructure


def create_number_filter_is_empty(property_name: str, is_empty: bool) -> NumberFilter:
    """
    Creates a NumberFilter that returns entries where the number property is empty.

    Args:
        property_name (str): The name of the property to filter.
        is_empty (bool): Whether to filter for empty or non-empty values.

    Returns:
        NumberFilter: The constructed NumberFilter object.
    """
    if is_empty:
        return NumberFilter(property=property_name, number=FilterStructure(is_empty=True))
    return NumberFilter(property=property_name, number=FilterStructure(is_not_empty=True))


def create_concrete_number_filter(
    property_name: str,
    filter_type: Literal[
        "does_not_equal",
        "equals",
        "greater_than",
        "greater_than_or_equal_to",
        "less_than",
        "less_than_or_equal_to",
    ],
    number_value: float,
) -> NumberFilter:
    """
    Creates a NumberFilter based on the provided filter type and value.

    Args:
        property_name (str): The name of the property to filter.
        filter_type (Literal): The type of filter to apply.
        number_value (float): The number value to compare against.

    Returns:
        NumberFilter: The constructed NumberFilter object.
    """
    number_filter_structure = FilterStructure()
    setattr(number_filter_structure, filter_type, number_value)
    return NumberFilter(property=property_name, number=number_filter_structure)


class IDFilter(Filter):
    """
    A filter class for applying an ID-based filter to a Notion database query.

    Attributes:
        property (str): The name of the property to apply the filter to.
        unique_id (FilterStructure): The filter criteria for the unique_id property.
    """

    unique_id: FilterStructure


def create_id_filter(
    property_name: str,
    filter_type: Literal[
        "equals",
        "does_not_equal",
        "greater_than",
        "greater_than_or_equal_to",
        "less_than",
        "less_than_or_equal_to",
    ],
    value: int,
) -> IDFilter:
    """
    Factory function to create an IDFilter object based on the provided filter type.

    Args:
        property_name (str): The name of the property to apply the unique_id filter to.
        filter_type (Literal): The type of filter to apply (e.g., 'equals', 'greater_than').
        value (int): The number to compare the unique_id property value against.

    Returns:
        IDFilter: The constructed IDFilter object with the specified property and filter criteria.
    """
    id_filter_structure = FilterStructure()
    setattr(id_filter_structure, filter_type, value)
    return IDFilter(property=property_name, unique_id=id_filter_structure)


__all__ = [
    "NumberFilter",
    "create_number_filter_is_empty",
    "create_concrete_number_filter",
    "IDFilter",
    "create_id_filter",
]
