from abc import ABC

from pydantic import BaseModel


class FilterStructure(BaseModel, extra='allow'):
    """
    Represents the inner filter structure used in notion database query api.
    """
    pass


class Filter(ABC, BaseModel, use_enum_values=True, from_attributes=True, arbitrary_types_allowed=True):
    property: str

    def serialize_to_json(self) -> dict:
        return self.model_dump(mode='json', exclude_none=True)


__all__ = ['FilterStructure', 'Filter']
