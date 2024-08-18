# Standard Library
from typing import Any


def remove_forbidden_properties_from_data(data: dict[str, Any], properties_to_remove: set[str]) -> dict[str, Any]:
    """
    Remove forbidden properties from the data dictionary before serialization as some properties like created_time,
    last_edited_time cannot be passed back to the Notion API.
    :param data: the data to remove the forbidden properties from.
    :param properties_to_remove: Properties to remove.
    :return: The data dictionary without the forbidden properties.
    """
    properties = data["_properties"]
    [properties.pop(key) for key, value in properties.items() if any(k in value for k in properties_to_remove)]
    return data
