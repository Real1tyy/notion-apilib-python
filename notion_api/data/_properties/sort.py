from typing import Literal

from pydantic import BaseModel


class Sort(BaseModel):
    direction: Literal['ascending', 'descending']

    def serialize_to_json(self) -> dict[str, str]:
        return self.model_dump(mode='json')


class PropertySort(Sort):
    property: str


class TimestampSort(Sort):
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
