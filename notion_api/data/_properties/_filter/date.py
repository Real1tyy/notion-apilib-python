# Standard Library
from datetime import datetime
from typing import Literal

from .general import Filter, FilterStructure


class DateFilter(Filter):
    """
     This class represents a filter for date properties in a database query.
     The filter is applied based on the structure provided in the `date` field.
     """
    date: FilterStructure


def create_date_filter_is_empty(property_name: str, is_empty: bool) -> DateFilter:
    """
    Creates a DateFilter that returns entries where the date property is empty.

    Args:
        property_name (str): The name of the property to filter.

    Returns:
        DateFilter: The constructed DateFilter object.
    """
    if is_empty:
        return DateFilter(property=property_name, date=FilterStructure(is_empty=True))
    return DateFilter(property=property_name, date=FilterStructure(is_not_empty=True))


def create_concrete_date_filter(
        property_name: str,
        filter_type: Literal['after', 'before', 'equals', 'on_or_after', 'on_or_before', 'next_month', 'next_week',
        'next_year', 'past_month', 'past_week', 'past_year', 'this_week'], date_value: datetime) -> DateFilter:
    """
    Creates a DateFilter based on the provided filter type.

    Args:
        property_name (str): The name of the property to filter.
        filter_type (Literal): The type of filter to apply.
        date_value (datetime): The date value to compare against

    Returns:
        DateFilter: The constructed DateFilter object.
    """
    date_filter_structure = FilterStructure()
    setattr(date_filter_structure, filter_type, date_value)
    return DateFilter(property=property_name, date=date_filter_structure)


def create_relative_date_filter(
        property_name: str, filter_type: Literal['next_month', 'next_week',
        'next_year', 'past_month', 'past_week', 'past_year', 'this_week']) -> DateFilter:
    """
    Creates a DateFilter based on the provided filter type, the filter type will be relative to the current timestamp.

    Args:
        property_name (str): The name of the property to filter.
        filter_type (Literal): The type of filter to apply.
        etc.

    Returns:
        DateFilter: The constructed DateFilter object.
    """
    date_filter_structure = FilterStructure()
    setattr(date_filter_structure, filter_type, {})
    return DateFilter(property=property_name, date=date_filter_structure)


__all__ = [
    "DateFilter",
    "create_date_filter_is_empty",
    'create_concrete_date_filter',
    'create_relative_date_filter'
]
