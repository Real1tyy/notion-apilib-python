from abc import ABC, abstractmethod
from typing import Any, Optional

from _filter.general import Filter

from pydantic import BaseModel, Field


class QueryFilter(ABC, BaseModel, extra='allow', from_attributes=True, arbitrary_types_allowed=True):
    """
    A model representing a query filter object for use during database querying.
    """

    @abstractmethod
    def add_additional_filter(self, filter_object: Any):
        pass

    @abstractmethod
    def add_nested_filter_object(self, nested_filter: 'QueryFilter'):
        pass

    @abstractmethod
    def get_current_filters(self) -> list[Filter]:
        pass

    @abstractmethod
    def get_nested_filter_object(self) -> 'QueryFilter':
        pass

    @abstractmethod
    def serialize_to_json(self) -> dict[str, Any]:
        pass


class AndFilter(QueryFilter):
    """
    A model representing an AND filter for a database query.
    """
    and_filter: list = Field(serialization_alias='and')

    def add_additional_filter(self, filter_object: Filter):
        self.and_filter.append(filter_object)

    def add_nested_filter_object(self, nested_filter: 'OrFilter'):
        for filter_object in self.and_filter:
            if isinstance(filter_object, OrFilter):
                filter_object.get_current_filters().extend(nested_filter.get_current_filters())
                return
        self.and_filter.append(nested_filter)

    def get_current_filters(self) -> list[Filter]:
        return self.and_filter

    def get_nested_filter_object(self) -> Optional['OrFilter']:
        for filter_object in self.and_filter:
            if isinstance(filter_object, OrFilter):
                return filter_object

    def serialize_to_json(self) -> dict[str, Any]:
        data = self.model_dump(mode='json')
        filter_data = data.pop('and_filter')
        data['and'] = filter_data
        key_to_remove = None
        for filter_object in filter_data:
            for key in filter_object.keys():
                if key == 'or_filter':
                    key_to_remove = key
                    break
            if key_to_remove:
                or_data = filter_object.pop(key_to_remove)
                filter_object['or'] = or_data
                break

        return data


class OrFilter(QueryFilter):
    """
    A model representing an AND filter for a database query.
    """
    or_filter: list = Field(serialization_alias='or')

    def add_additional_filter(self, filter_object: Filter):
        self.or_filter.append(filter_object)

    def add_nested_filter_object(self, nested_filter: 'OrFilter'):
        for filter_object in self.or_filter:
            if isinstance(filter_object, AndFilter):
                filter_object.get_current_filters().extend(nested_filter.get_current_filters())
                return
        self.or_filter.append(nested_filter)

    def get_current_filters(self) -> list[Filter]:
        return self.or_filter

    def get_nested_filter_object(self) -> Optional[AndFilter]:
        for filter_object in self.or_filter:
            if isinstance(filter_object, AndFilter):
                return filter_object

    def serialize_to_json(self) -> dict[str, Any]:
        data = self.model_dump(mode='json')
        filter_data = data.pop('or_filter')
        data['or'] = filter_data
        key_to_remove = None
        for filter_object in filter_data:
            for key in filter_object.keys():
                if key == 'and_filter':
                    key_to_remove = key
                    break
            if key_to_remove:
                or_data = filter_object.pop(key_to_remove)
                filter_object['and'] = or_data
                break

        return data


def create_and_filter(and_filter: list[Filter]) -> AndFilter:
    return AndFilter(and_filter=and_filter)


def create_or_filter(or_filter: list[Filter]) -> OrFilter:
    return OrFilter(or_filter=or_filter)


__all__ = ['QueryFilter', 'create_and_filter', 'create_or_filter', 'AndFilter', 'OrFilter']
