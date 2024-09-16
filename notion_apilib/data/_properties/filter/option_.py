# Third Party
from pydantic import BaseModel

from ._general import Filter, FilterStructure


class CheckboxFilterStructure(BaseModel):
    """
    Represents the structure for the checkbox filter criteria in a Notion database query.

    Attributes:
        equals (bool): The boolean value to compare the checkbox property against.
                       Defaults to True, meaning the filter will match entries where the checkbox is checked.
    """

    equals: bool = True


class CheckboxFilter(Filter):
    """
    A filter class for applying a checkbox-based filter to a Notion database query.

    Attributes:
        property (str): The name of the property to apply the filter to.
        checkbox (CheckboxFilterStructure): The filter criteria for the checkbox property.
    """

    checkbox: CheckboxFilterStructure


def create_checkbox_filter(property_name: str, equals: bool) -> CheckboxFilter:
    """
    Factory function to create a CheckboxFilter object.

    Args:
        property_name (str): The name of the property to apply the checkbox filter to.
        equals (bool): The boolean value to compare the checkbox property against.

    Returns:
        CheckboxFilter: The constructed CheckboxFilter object with the specified property and filter criteria.
    """
    return CheckboxFilter(property=property_name, checkbox=CheckboxFilterStructure(equals=equals))


class MultiSelectFilter(Filter):
    """
    A filter class for applying a multi-select-based filter to a Notion database query.

    Attributes:
        property (str): The name of the property to apply the filter to.
        multi_select (MultiSelectFilterStructure): The filter criteria for the multi-select property.
    """

    multi_select: FilterStructure


def create_multi_select_filter_contains(property_name: str, contains: str) -> MultiSelectFilter:
    """
    Factory function to create a MultiSelectFilter object.

    Args:
        property_name (str): The name of the property to apply the multi-select filter to.
        contains (str): The string to check if the multi-select property contains.

    Returns:
        MultiSelectFilter: The constructed MultiSelectFilter object with the specified property and filter criteria.
    """
    return MultiSelectFilter(property=property_name, multi_select=FilterStructure(contains=contains))


def create_multi_select_filter_does_not_contains(property_name: str, does_not_contain: str) -> MultiSelectFilter:
    """
    Factory function to create a MultiSelectFilter object.

    Args:
        property_name (str): The name of the property to apply the multi-select filter to.
        does_not_contain (str): The string to check if the multi-select property does not contain.

    Returns:
        MultiSelectFilter: The constructed MultiSelectFilter object with the specified property and filter criteria.
    """
    return MultiSelectFilter(
        property=property_name,
        multi_select=FilterStructure(does_not_contain=does_not_contain),
    )


def create_multi_select_filter_is_empty(property_name: str, is_empty: bool) -> MultiSelectFilter:
    """
    Factory function to create a MultiSelectFilter object.

    Args:
        is_empty (bool): Whether the property should be empty or not

    Returns:
        MultiSelectFilter: The constructed MultiSelectFilter object with the specified property and filter criteria.
    """
    if is_empty:
        return MultiSelectFilter(property=property_name, multi_select=FilterStructure(is_empty=True))
    return MultiSelectFilter(property=property_name, multi_select=FilterStructure(is_not_empty=True))


class SelectFilter(Filter):
    """
    A filter class for applying a select-based filter to a Notion database query.

    Attributes:
        property (str): The name of the property to apply the filter to.
        select (FilterStructure): The filter criteria for the select property.
    """

    select: FilterStructure


def create_select_filter_equals(property_name: str, equals: str) -> SelectFilter:
    """
    Factory function to create a SelectFilter object that checks if the select property equals a specific value.

    Args:
        property_name (str): The name of the property to apply the select filter to.
        equals (str): The string to compare the select property value against.

    Returns:
        SelectFilter: The constructed SelectFilter object with the specified property and filter criteria.
    """
    return SelectFilter(property=property_name, select=FilterStructure(equals=equals))


def create_select_filter_does_not_equal(property_name: str, does_not_equal: str) -> SelectFilter:
    """
    Factory function to create a SelectFilter object that checks if the select property does not equal a specific value.

    Args:
        property_name (str): The name of the property to apply the select filter to.
        does_not_equal (str): The string to compare the select property value against.

    Returns:
        SelectFilter: The constructed SelectFilter object with the specified property and filter criteria.
    """
    return SelectFilter(property=property_name, select=FilterStructure(does_not_equal=does_not_equal))


def create_select_filter_is_empty(property_name: str, is_empty: bool) -> SelectFilter:
    """
    Factory function to create a SelectFilter object that checks if the select property is empty or not.

    Args:
        property_name (str): The name of the property to apply the select filter to.
        is_empty (bool): Whether to check if the select property is empty or not.

    Returns:
        SelectFilter: The constructed SelectFilter object with the specified property and filter criteria.
    """
    if is_empty:
        return SelectFilter(property=property_name, select=FilterStructure(is_empty=True))
    return SelectFilter(property=property_name, select=FilterStructure(is_not_empty=True))


class StatusFilter(Filter):
    """
    A filter class for applying a status-based filter to a Notion database query.

    Attributes:
        property (str): The name of the property to apply the filter to.
        status (FilterStructure): The filter criteria for the status property.
    """

    status: FilterStructure


def create_status_filter_equals(property_name: str, equals: str) -> StatusFilter:
    """
    Factory function to create a StatusFilter object that checks if the status property equals a specific value.

    Args:
        property_name (str): The name of the property to apply the status filter to.
        equals (str): The string to compare the status property value against.

    Returns:
        StatusFilter: The constructed StatusFilter object with the specified property and filter criteria.
    """
    return StatusFilter(property=property_name, status=FilterStructure(equals=equals))


def create_status_filter_does_not_equal(property_name: str, does_not_equal: str) -> StatusFilter:
    """
    Factory function to create a StatusFilter object that checks if the status property does not equal a specific value.

    Args:
        property_name (str): The name of the property to apply the status filter to.
        does_not_equal (str): The string to compare the status property value against.

    Returns:
        StatusFilter: The constructed StatusFilter object with the specified property and filter criteria.
    """
    return StatusFilter(property=property_name, status=FilterStructure(does_not_equal=does_not_equal))


def create_status_filter_is_empty(property_name: str, is_empty: bool) -> StatusFilter:
    """
    Factory function to create a StatusFilter object that checks if the status property is empty or not.

    Args:
        property_name (str): The name of the property to apply the status filter to.
        is_empty (bool): Whether to check if the status property is empty or not.

    Returns:
        StatusFilter: The constructed StatusFilter object with the specified property and filter criteria.
    """
    if is_empty:
        return StatusFilter(property=property_name, status=FilterStructure(is_empty=True))
    return StatusFilter(property=property_name, status=FilterStructure(is_not_empty=True))


__all__ = [
    "CheckboxFilter",
    "create_checkbox_filter",
    "create_multi_select_filter_contains",
    "create_multi_select_filter_is_empty",
    "SelectFilter",
    "create_select_filter_equals",
    "create_select_filter_is_empty",
    "StatusFilter",
    "create_status_filter_equals",
    "create_status_filter_is_empty",
    "MultiSelectFilter",
    "create_multi_select_filter_does_not_contains",
    "create_status_filter_does_not_equal",
    "create_select_filter_does_not_equal",
]
