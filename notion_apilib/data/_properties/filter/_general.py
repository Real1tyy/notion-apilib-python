# Standard Library
from abc import ABC

# Third Party
from pydantic import BaseModel

# First Party
from notion_apilib.data.configuration_ import BasicConfiguration


class FilterStructure(BaseModel, extra="allow"):
    """
    Represents the inner filter structure used in notion database query api.
    """

    pass


class Filter(BasicConfiguration, ABC):
    property: str

    def serialize_to_json(self) -> dict:
        return self.model_dump(mode="json", exclude_none=True)


__all__ = ["FilterStructure", "Filter"]
