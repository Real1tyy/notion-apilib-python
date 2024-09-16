# Standard Library
from typing import Any, Callable, Generic, Type, TypeVar

# Third Party
from pydantic import Field, model_validator

# First Party
from notion_apilib.data.properties import Property

from .configuration_ import ExtraConfiguration
from .properties import (
    DatabaseProperty,
    PageProperty,
    TitleDatabase,
    TitlePage,
    deserialize_database_property,
    deserialize_page_property,
)
from .structures import RichText

T = TypeVar("T", bound=Property)


class PropertiesStructure(ExtraConfiguration, Generic[T]):
    properties: list[T] = Field(exclude=True, default=[])

    def __len__(self) -> int:
        return len(self.properties)

    def __iter__(self):
        return iter(self.properties)


class PagePropertiesStructure(PropertiesStructure[PageProperty]):
    title_structure_model: TitlePage = Field(alias="title")

    @property
    def title(self) -> str:
        """
        gets the value of the title Page property, note that the value is returned as a plain text, so any formatting
        is ignored, if you want specific formatting, you should use the title_structure attribute
        :return: plain text value of the title
        """
        return self.title_structure_model.title

    @title.setter
    def title(self, value: str):
        """
        sets the value of the title Page property, note that the value is expected to be plain text, so any formatting
        will be ignored, if you want specific formatting, you should use the title_structure attribute, also note
        that any previous value or formatting will be overwritten to plain text
        :param value: value to set - plain text
        :return: None
        """
        self.title_structure_model.title = value

    @property
    def title_structure(self) -> list[RichText]:
        """
        :return: The title value of the page, in rich text format.
        """
        return self.title_structure_model.title_structure

    @title_structure.setter
    def title_structure(self, value: list[RichText]) -> None:
        """
        sets the value of the title Page property, the value is expected to be a list of rich text so with formatting
        :param value: rich text value to be set
        :return: None
        """
        self.title_structure_model.title_structure = value

    @model_validator(mode="before")
    def parse_properties(cls, v: Any):
        return parse_properties_structure(v, deserialize_page_property, TitlePage)


class DatabasePropertiesStructure(PropertiesStructure[DatabaseProperty]):
    @model_validator(mode="before")
    def parse_properties(cls, v: Any):
        return parse_properties_structure(
            v, deserialize_database_property, TitleDatabase
        )


def parse_properties_structure(
    v: dict,
    deserialization_func: Callable[[dict], Property],
    title_property_type: Type[Property],
) -> dict:
    properties = []
    title = None
    for key, value in v.items():
        value["name"] = key
        _class = deserialization_func(value)
        properties.append(_class)
        v[key] = _class
        if isinstance(_class, title_property_type):
            title = _class
    if title is None:
        raise ValueError("Title property not found")

    v["title"] = title
    v["properties"] = properties
    return v
