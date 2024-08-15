from typing import Literal
from .general import FilterStructure, Filter


class RichTextFilter(Filter):
    """
    A filter class for applying a rich text-based filter to a Notion database query.

    Attributes:
        property (str): The name of the property to apply the filter to.
        rich_text (FilterStructure): The filter criteria for the rich text property.
    """
    rich_text: FilterStructure


def create_rich_text_filter_is_empty(property_name: str, is_empty: bool) -> RichTextFilter:
    """
    Creates a DateFilter that returns entries where the date property is empty.

    Args:
        property_name (str): The name of the property to filter.

    Returns:
        DateFilter: The constructed DateFilter object.
    """
    if is_empty:
        return RichTextFilter(property=property_name, date=FilterStructure(is_empty=True))
    return RichTextFilter(property=property_name, date=FilterStructure(is_not_empty=True))


def create_rich_text_filter(
        property_name: str,
        filter_type: Literal['contains', 'does_not_contain', 'does_not_equal', 'ends_with',
        'equals', 'starts_with'], text_value: str) -> RichTextFilter:
    """
    Factory function to create a RichTextFilter object based on the provided filter type and text value.

    Args:
        property_name (str): The name of the property to apply the rich text filter to.
        filter_type (Literal): The type of filter to apply.
        text_value (str): The text value to compare against. Required for most filter types.

    Returns:
        RichTextFilter: The constructed RichTextFilter object with the specified property and filter criteria.
    """
    rich_text_filter_structure = FilterStructure()
    setattr(rich_text_filter_structure, filter_type, text_value)
    return RichTextFilter(property=property_name, rich_text=rich_text_filter_structure)


__all__ = [
    "RichTextFilter",
    "create_rich_text_filter",
    'create_rich_text_filter_is_empty'
]
