from typing import Literal

from pydantic import BaseModel

from .date import DateFilter


class TimestampFilter(BaseModel, extra='allow'):
    """
    A filter class for applying a timestamp-based filter to a Notion database query.

    Attributes:
        timestamp (Literal['created_time', 'last_edited_time']): The type of timestamp to filter.
    """
    timestamp: Literal['created_time', 'last_edited_time']


def create_timestamp_filter(
        timestamp_type: Literal['created_time', 'last_edited_time'],
        date_filter: DateFilter) -> TimestampFilter:
    """
    Factory function to create a TimestampFilter object.

    Args:
        timestamp_type (Literal): The type of timestamp to filter ('created_time', 'last_edited_time').
        date_filter (DateFilter): The filter criteria for the timestamp.

    Returns:
        TimestampFilter: The constructed TimestampFilter object with the specified property and filter criteria.
    """
    filter_structure = TimestampFilter(timestamp=timestamp_type)
    data = date_filter.serialize_to_json()
    date_data = data.pop('date')
    setattr(filter_structure, timestamp_type, date_data)
    return filter_structure


__all__ = [
    "TimestampFilter",
    "create_timestamp_filter",
]
