from .general_ import Filter, FilterStructure


class FilesFilter(Filter):
    """
    A filter class for applying a file-based filter to a Notion database query.

    Attributes:
        property (str): The name of the property to apply the filter to.
        files (FilesFilterStructure): The filter criteria for the file property, specifying whether it is empty.
    """

    files: FilterStructure


def create_files_filter_is_empty(property_name: str, is_empty: bool) -> FilesFilter:
    """
    Factory function to create a FilesFilter object.

    Args:
        property_name (str): The name of the property to apply the files filter to.

    Returns:
        FilesFilter: The constructed FilesFilter object with the specified property and filter criteria.
    """
    if is_empty:
        return FilesFilter(property=property_name, files=FilterStructure(is_empty=True))
    return FilesFilter(property=property_name, files=FilterStructure(is_not_empty=True))


__all__ = ["FilesFilter", "create_files_filter_is_empty"]
