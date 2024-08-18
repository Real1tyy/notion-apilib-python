# Standard Library
from abc import ABC, abstractmethod
from typing import Any, Optional

# Third Party
from pydantic import Field

# First Party
from notion_apilib.data.configuration_ import ExtraConfiguration

from ._general import Filter


class QueryFilter(ExtraConfiguration, ABC):
    """
    A model representing a query filter object for use during database querying.
    """

    @abstractmethod
    def add_additional_filter(self, filter_object: Any):
        pass

    @abstractmethod
    def add_nested_filter_object(self, nested_filter: "QueryFilter"):
        pass

    @abstractmethod
    def get_current_filters(self) -> list[Filter]:
        pass

    @abstractmethod
    def get_nested_filter_object(self) -> "QueryFilter":
        pass

    def serialize_to_json(self) -> dict[str, Any]:
        return self.json_dump()


class AndFilter(QueryFilter):
    """
    A model representing an AND filter for a database query.
    """

    and_filter: list = Field(serialization_alias="and")

    def add_additional_filter(self, filter_object: Filter):
        self.and_filter.append(filter_object)

    def add_nested_filter_object(self, nested_filter: "OrFilter"):
        filter_object = self.get_nested_filter_object()
        if filter_object:
            filter_object.get_current_filters().extend(nested_filter.get_current_filters())
            return
        self.and_filter.append(nested_filter)

    def get_current_filters(self) -> list[Filter]:
        return self.and_filter

    def get_nested_filter_object(self) -> Optional["OrFilter"]:
        for filter_object in self.and_filter:
            if isinstance(filter_object, OrFilter):
                return filter_object


class OrFilter(QueryFilter):
    """
    A model representing an AND filter for a database query.
    """

    or_filter: list = Field(serialization_alias="or")

    def add_additional_filter(self, filter_object: Filter):
        self.or_filter.append(filter_object)

    def add_nested_filter_object(self, nested_filter: "OrFilter"):
        filter_object = self.get_nested_filter_object()
        if filter_object:
            filter_object.get_current_filters().extend(nested_filter.get_current_filters())
            return
        self.or_filter.append(nested_filter)

    def get_current_filters(self) -> list[Filter]:
        return self.or_filter

    def get_nested_filter_object(self) -> Optional[AndFilter]:
        for filter_object in self.or_filter:
            if isinstance(filter_object, AndFilter):
                return filter_object


def create_and_filter(and_filter: list[Filter]) -> AndFilter:
    return AndFilter(and_filter=and_filter)


def create_or_filter(or_filter: list[Filter]) -> OrFilter:
    return OrFilter(or_filter=or_filter)


__all__ = [
    "QueryFilter",
    "create_and_filter",
    "create_or_filter",
    "AndFilter",
    "OrFilter",
]
