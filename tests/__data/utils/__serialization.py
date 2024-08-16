# Standard Library
from datetime import datetime
from typing import Any, Callable, TypeVar
from uuid import UUID

T = TypeVar("T")


def map_data(data: T, value_transform: Callable[[Any], Any]) -> T:
    """
    Recursively apply a transformation to all values in a dictionary or list.

    :param data: The data to transform.
    :param value_transform: A function that transforms a value.
    :return: The transformed data.
    """
    if isinstance(data, list):
        return [map_data(item, value_transform) for item in data]

    if isinstance(data, dict):
        return {key: map_data(value, value_transform) for key, value in data.items()}

    return value_transform(data)


def filter_data(
        data: T, key_predicate: Callable[[Any], bool] = None, value_predicate: Callable[[Any], bool] = None) -> T:
    """
    Recursively filter out items from a dictionary or list based on key or value predicates.

    :param data: The data to filter.
    :param key_predicate: A function that returns True for keys to be removed.
    :param value_predicate: A function that returns True for values to be removed.
    :return: The filtered data with items removed based on the predicates.
    """
    if isinstance(data, list):
        return [filter_data(item, key_predicate, value_predicate) for item in data]

    if isinstance(data, dict):
        filtered_dict = {}
        for key, value in data.items():
            # Check if the key should be excluded based on the key_predicate
            if key_predicate is not None and key_predicate(key):
                continue

            # Recursively filter the value
            filtered_value = filter_data(value, key_predicate, value_predicate)

            # Check if the value should be excluded based on the value_predicate
            if value_predicate is not None and value_predicate(filtered_value):
                continue

            # If both the key and value pass the filters, add them to the filtered_dict
            filtered_dict[key] = filtered_value

        return filtered_dict
    return data


# Specific use cases:
def remove_none_values(data: T) -> T:
    """
    Recursively remove all None values from a dictionary or list.

    :param data: The data to clean.
    :return: The cleaned data with no None values.
    """
    return filter_data(data, value_predicate=lambda x: x is None)


def remove_children_keys(data: T) -> T:
    """
    Recursively remove all 'children' keys from a dictionary or list.

    :param data: The data to clean.
    :return: The cleaned data with no 'children' keys.
    """
    return filter_data(data, key_predicate=lambda key: key == 'children')


def transform_uuid_to_string(data: T) -> T:
    """
    Recursively transform all UUID values in a dictionary or list into strings.

    :param data: The data to transform.
    :return: The transformed data with UUIDs as strings.
    """

    def value_predicate(value: Any) -> Any:
        if isinstance(value, UUID):
            return str(value)
        return value

    return map_data(data, value_predicate)


def transform_datetime_to_string(data: T) -> T:
    """
    Recursively transform all datetime values in a dictionary or list into strings.

    :param data: The data to transform.
    :return: The transformed data with datetimes as strings.
    """

    def value_predicate(value: Any) -> Any:
        if isinstance(value, datetime):
            return value.strftime("%Y-%m-%dT%H:%M:%SZ")
        return value

    return map_data(data, value_predicate)


def transform_dictionary(dictionary: dict) -> dict:
    """
    Transform a dictionary by removing None values, 'children' keys, UUIDs, and datetimes.

    :param dictionary: The dictionary to transform.
    :return: The transformed dictionary.
    """
    transformed = remove_none_values(dictionary)
    transformed = remove_children_keys(transformed)
    transformed = transform_uuid_to_string(transformed)
    transformed = transform_datetime_to_string(transformed)
    return transformed
