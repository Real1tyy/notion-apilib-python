# Standard Library
from typing import Any

# Third Party
from pydantic import Field

from ._util import remove_forbidden_properties_from_data
from .structures import RichText
# First Party
from .object_ import MajorObject
from .properties_structure import PagePropertiesStructure
from notion_apilib.data.properties import PageProperty
from notion_apilib.data.blocks import Block


class Page(MajorObject):
    properties_attributes: PagePropertiesStructure = Field(alias="properties")
    children: list[Block] = Field(default=[])

    @property
    def properties(self) -> list[PageProperty]:
        return self.properties_attributes.properties

    def serialize_to_json(self) -> dict[str, Any]:
        """
        Serialize the page to JSON. Excludes the id, archived, and children properties. As well as properties that are
        either rollup, formula, last_edited_time, created_time, or unique_id.
        :return: The serialized page j.
        """
        data = self.json_dump({"id", "archived", "children"})
        keys_to_check = {"rollup", "formula", "last_edited_time", "created_time", "unique_id"}
        return remove_forbidden_properties_from_data(data, keys_to_check)

    def add_property(self, property_: PageProperty) -> None:
        self.properties.append(property_)
        setattr(self.properties_attributes, property_.name, property_)

    @property
    def title(self) -> str:
        """
        gets the value of the title Page property, note that the value is returned as a plain text, so any formatting
        is ignored, if you want specific formatting, you should use the title_structure attribute
        :return: plain text value of the title
        """
        return self.properties_attributes.title

    @title.setter
    def title(self, value: str):
        """
        sets the value of the title Page property, note that the value is expected to be plain text, so any formatting
        will be ignored, if you want specific formatting, you should use the title_structure attribute, also note
        that any previous value or formatting will be overwritten to plain text
        :param value: value to set - plain text
        :return: None
        """
        self.properties_attributes.title = value

    @property
    def title_structure(self) -> list[RichText]:
        """
        :return: The title value of the page, in rich text format.
        """
        return self.properties_attributes.title_structure

    @title_structure.setter
    def title_structure(self, value: list[RichText]) -> None:
        """
        sets the value of the title Page property, the value is expected to be a list of rich text so with formatting
        :param value: rich text value to be set
        :return: None
        """
        self.properties_attributes.title_structure = value


def deserialize_page(data: dict[str, Any]) -> Page:
    return Page(**data)


__all__ = ["Page", "deserialize_page"]
