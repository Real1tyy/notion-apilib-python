# Standard Library
from typing import Any

# Third Party
from pydantic import Field

# First Party
from .object_ import MajorObject
from .page_ import Page
from .properties_structure import PropertiesStructure
from notion_api.data.properties import DatabaseProperty
from notion_api.data.structures import RichText


class Database(MajorObject):
    title_structure: list[RichText] = Field(alias="title")
    description: list[RichText]
    is_inline: bool
    properties_attributes: PropertiesStructure[DatabaseProperty] = Field(alias="properties")
    pages: list[Page] = Field(default=[], exclude=True)

    @property
    def properties(self) -> list[DatabaseProperty]:
        return self.properties_attributes.properties

    def serialize_to_json(self) -> dict[str, Any]:
        data = super().json_dump({"id", "archived", "last_edited_time", "created_time"})
        properties = data["_properties"]
        keys_to_check = {"rollup", "formula", "relation", "unique_id"}
        [
            properties.pop(key)
            for key, value in properties.items()
            if any(k in value for k in keys_to_check)
        ]
        return data

    def add_property(self, property_: DatabaseProperty) -> None:
        self.properties.append(property_)
        setattr(self.properties, property_.name, property_)

    @property
    def title(self) -> str:
        """
        gets the value of the title Page property, note that the value is returned as a plain text, so any formatting
        is ignored, if you want specific formatting, you should use the title_structure attribute
        :return: plain text value of the title
        """
        return self.title_structure

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


def deserialize_database(data: dict[str, Any]) -> Database:
    return Database(**data)


__all__ = ["Database", "deserialize_database"]
