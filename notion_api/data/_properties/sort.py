from typing import Literal

from pydantic import BaseModel


class Sort(BaseModel):
    """
    Base class for sorting options in a Notion database query.

    Attributes:
        direction (Literal['ascending', 'descending']): The direction in which to sort the results.
    """

    direction: Literal['ascending', 'descending']

    def serialize_to_json(self) -> dict[str, str]:
        """
        Serializes the sort object to a JSON-compatible dictionary.

        Returns:
            dict[str, str]: The serialized dictionary of the sort object.
        """
        return self.model_dump(mode='json')


class PropertySort(Sort):
    """
    Class for sorting based on a specific property in a Notion database query.

    Attributes:
        property (str): The name of the property to sort by.
        direction (Literal['ascending', 'descending']): The direction in which to sort the results.
    """

    property: str


class TimestampSort(Sort):
    """
    Class for sorting based on timestamps in a Notion database query.

    Attributes:
        timestamp (Literal['created_time', 'last_edited_time']): The timestamp field to sort by.
        direction (Literal['ascending', 'descending']): The direction in which to sort the results.
    """

    timestamp: Literal['created_time', 'last_edited_time']


def create_created_time_sort(direction: Literal['ascending', 'descending']) -> 'TimestampSort':
    """
      Creates a sort object for the created time property timestamp with the specified sort direction.
    :param direction: direction - ascending / descending
    :return: TimestampSort object representing the sorting
    """
    return TimestampSort(timestamp='created_time', direction=direction)


def create_last_edited_time_sort(direction: Literal['ascending', 'descending']) -> 'TimestampSort':
    """
      Creates a sort object for the last edited time property timestamp with the specified sort direction.
    :param direction: direction - ascending / descending
    :return: TimestampSort object representing the sorting
    """
    return TimestampSort(timestamp='last_edited_time', direction=direction)


def created_sort_object(name: str, direction: Literal['ascending', 'descending']) -> 'PropertySort':
    """
      Creates a sort object for the property with the specified sort direction.
    :param name: name of the property
    :param direction: direction - ascending / descending
    :return PropertySort object representing the sorting
    """
    return PropertySort(direction=direction, property=name)


__all__ = ['Sort', 'PropertySort', 'TimestampSort', 'create_created_time_sort', 'create_last_edited_time_sort',
           'created_sort_object']
