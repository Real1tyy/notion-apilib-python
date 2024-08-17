# Standard Library
from typing import Any

# Third Party
from pydantic import Field

# First Party
from notion_apilib.data.properties import DatabaseProperty
from notion_apilib.data.structures import FormatedText

from ._util import remove_forbidden_properties_from_data
from .object_ import MajorObject
from .page_ import Page
from .properties_structure import DatabasePropertiesStructure


class Database(MajorObject):
    title_structure: FormatedText = Field(alias="title")
    description_structure: FormatedText = Field(alias="description")
    is_inline: bool
    properties_attributes: DatabasePropertiesStructure = Field(alias="properties")
    pages: list[Page] = Field(default=[], exclude=True)

    @property
    def properties(self) -> list[DatabaseProperty]:
        return self.properties_attributes.properties

    def serialize_to_json(self) -> dict[str, Any]:
        data = self.json_dump({"id", "archived", "last_edited_time", "created_time"})
        keys_to_check = {"rollup", "formula", "relation", "unique_id"}
        return remove_forbidden_properties_from_data(data, keys_to_check)

    def add_property(self, property_: DatabaseProperty) -> None:
        self.properties.append(property_)
        setattr(self.properties_attributes, property_.name, property_)

    @property
    def title(self) -> str:
        """
        gets the value of the title Page property, note that the value is returned as a plain text, so any formatting
        is ignored, if you want specific formatting, you should use the title_structure attribute
        :return: plain text value of the title
        """
        return self.title_structure.text

    @title.setter
    def title(self, value: str):
        """
        sets the value of the title Page property, note that the value is expected to be plain text, so any formatting
        will be ignored, if you want specific formatting, you should use the title_structure attribute, also note
        that any previous value or formatting will be overwritten to plain text
        :param value: value to set - plain text
        :return: None
        """
        self.title_structure.text = value

    @property
    def description(self) -> str:
        """
        returns the description of the database
        :return: description of the database in plain text
        """
        return self.description_structure.text

    @description.setter
    def description(self, value: str):
        """
        sets the value of the description of the database, the value is expected to be plain text, so any formatting
        will be ignored, if you want specific formatting, you should use the description_structure attribute, also note
        that any previous value or formatting will be overwritten to plain text
        :param value: value to set - plain text
        :return: None
        """
        self.description_structure.text = value


def deserialize_database(data: dict[str, Any]) -> Database:
    return Database(**data)


__all__ = ["Database", "deserialize_database"]
