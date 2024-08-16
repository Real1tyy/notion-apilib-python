# Standard Library
from typing import Callable, TypeVar, Generic

# Third Party
from pydantic import Field

# First Party
from .configuration_ import ExtraConfiguration
from notion_api.data.properties import Property

T = TypeVar("T", bound=Property)


class PropertiesStructure(ExtraConfiguration, Generic[T]):
    properties: list[T] = Field(exclude=True, default=[])


def parse_properties(
        v: dict, deserialization_func: Callable[[dict], Property]
) -> PropertiesStructure:
    properties = []
    for key, value in v.items():
        value["name"] = key
        _class = deserialization_func(value)
        properties.append(_class)
        v[key] = _class

    v["properties"] = properties
    return v
