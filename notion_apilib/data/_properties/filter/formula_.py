from ._general import Filter, FilterStructure
from .date_ import DateFilter
from .number_ import NumberFilter
from .text_ import RichTextFilter


class FormulaFilter(Filter):
    """
    A filter class for applying a formula-based filter to a Notion database query.

    Attributes:
        property (str): The name of the property to apply the filter to.
        formula (FormulaFilterStructure): The filter criteria for the formula property,
                                          which can contain conditions for different types.
    """

    formula: FilterStructure


def create_formula_checkbox_filter(property_name: str, checkbox_filter: "CheckboxFilter") -> FormulaFilter:
    """
    Factory function to create a FormulaFilter object with a checkbox condition.

    Args:
        property_name (str): The name of the property to apply the formula filter to.
        checkbox_filter (dict): A dictionary representing the checkbox filter condition.

    Returns:
        FormulaFilter: The constructed FormulaFilter object with the specified property and checkbox condition.
    """
    data = checkbox_filter.serialize_to_json()
    checkbox = data.pop("checkbox")
    return FormulaFilter(property=property_name, formula=FilterStructure(checkbox=checkbox))


def create_formula_date_filter(property_name: str, date_filter: DateFilter) -> FormulaFilter:
    """
    Factory function to create a FormulaFilter object with a date condition.

    Args:
        property_name (str): The name of the property to apply the formula filter to.
        date_filter (dict): A dictionary representing the date filter condition.

    Returns:
        FormulaFilter: The constructed FormulaFilter object with the specified property and date condition.
    """
    data = date_filter.serialize_to_json()
    date = data.pop("date")
    return FormulaFilter(property=property_name, formula=FilterStructure(date=date))


def create_formula_number_filter(property_name: str, number_filter: NumberFilter) -> FormulaFilter:
    """
    Factory function to create a FormulaFilter object with a number condition.

    Args:
        property_name (str): The name of the property to apply the formula filter to.
        number_filter (dict): A dictionary representing the number filter condition.

    Returns:
        FormulaFilter: The constructed FormulaFilter object with the specified property and number condition.
    """
    data = number_filter.serialize_to_json()
    number = data.pop("number")
    return FormulaFilter(property=property_name, formula=FilterStructure(number=number))


def create_formula_string_filter(property_name: str, string_filter: RichTextFilter) -> FormulaFilter:
    """
    Factory function to create a FormulaFilter object with a string condition.

    Args:
        property_name (str): The name of the property to apply the formula filter to.
        string_filter (dict): A dictionary representing the string (rich text) filter condition.

    Returns:
        FormulaFilter: The constructed FormulaFilter object with the specified property and string condition.
    """
    data = string_filter.serialize_to_json()
    rich_text = data.pop("rich_text")
    return FormulaFilter(property=property_name, formula=FilterStructure(string=rich_text))


__all__ = [
    "FormulaFilter",
    "create_formula_checkbox_filter",
    "create_formula_date_filter",
    "create_formula_number_filter",
    "create_formula_string_filter",
]
