from .general_ import Filter, FilterStructure


class PeopleFilter(Filter):
    """
    A filter class for applying a people-based filter to a Notion database query.

    Attributes:
        property (str): The name of the property to apply the filter to.
        people (FilterStructure): The filter criteria for the people property.
    """

    people: FilterStructure


def create_people_filter_contains(property_name: str, contains: str) -> PeopleFilter:
    """
    Factory function to create a PeopleFilter object that checks if the people property contains a specific UUID.

    Args:
        property_name (str): The name of the property to apply the people filter to.
        contains (str): The UUID to check if the people property contains.

    Returns:
        PeopleFilter: The constructed PeopleFilter object with the specified property and filter criteria.
    """
    return PeopleFilter(
        property=property_name, people=FilterStructure(contains=contains)
    )


def create_people_filter_does_not_contain(
    property_name: str, does_not_contain: str
) -> PeopleFilter:
    """
    Factory function to create a PeopleFilter object that checks if the people property does not contain a specific UUID.

    Args:
        property_name (str): The name of the property to apply the people filter to.
        does_not_contain (str): The UUID to check if the people property does not contain.

    Returns:
        PeopleFilter: The constructed PeopleFilter object with the specified property and filter criteria.
    """
    return PeopleFilter(
        property=property_name,
        people=FilterStructure(does_not_contain=does_not_contain),
    )


def create_people_filter_is_empty(property_name: str, is_empty: bool) -> PeopleFilter:
    """
    Factory function to create a PeopleFilter object that checks if the people property is empty or not.

    Args:
        property_name (str): The name of the property to apply the people filter to.
        is_empty (bool): Whether to check if the people property is empty or not.

    Returns:
        PeopleFilter: The constructed PeopleFilter object with the specified property and filter criteria.
    """
    if is_empty:
        return PeopleFilter(
            property=property_name, people=FilterStructure(is_empty=True)
        )
    return PeopleFilter(
        property=property_name, people=FilterStructure(is_not_empty=True)
    )


__all__ = [
    "PeopleFilter",
    "create_people_filter_contains",
    "create_people_filter_does_not_contain",
    "create_people_filter_is_empty",
]
