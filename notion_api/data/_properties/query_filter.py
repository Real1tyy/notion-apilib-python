from abc import ABC

from pydantic import BaseModel, Field


class Filter(ABC, BaseModel, use_enum_values=True, from_attributes=True, arbitrary_types_allowed=True):
    property: str

    def serialize_to_json(self) -> dict:
        return self.model_dump(mode='json', exclude_none=True)


class QueryFilterOptions(BaseModel):
    or_filter: list = Field(default_factory=list, serialization_alias='or')
    and_filter: list = Field(default_factory=list, serialization_alias='and')


class QueryFilter(BaseModel):
    """
    A model representing a query filter object for use during database querying.
    """
    filter: QueryFilterOptions = Field(default=QueryFilterOptions())


__all__ = ['QueryFilter', 'QueryFilterOptions', 'Filter']
