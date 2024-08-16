# Standard Library
from typing import Any

# Third Party
from pydantic import Field, field_validator

# First Party
from .object_ import MajorObject
from .properties_structure import PropertiesStructure, parse_properties
from notion_api.data.properties import PageProperty, deserialize_page_property
from notion_api.data.blocks import Block


class Page(MajorObject):
    properties_attributes: PropertiesStructure[PageProperty] = Field(alias="properties")
    children: list[Block] = Field(default=[])

    @field_validator("properties_attributes", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> PropertiesStructure:
        return parse_properties(v, deserialize_page_property)

    @property
    def properties(self) -> list[PageProperty]:
        return self.properties_attributes.properties

    def serialize_to_json(self) -> dict[str, Any]:
        """
        Serialize the page to JSON. Excludes the id, archived, and children properties. As well as properties that are
        either rollup, formula, last_edited_time, created_time, or unique_id.
        :return: The serialized page j.
        """
        data = self.model_dump(
            mode="json", exclude_none=True, exclude={"id", "archived", "children"}
        )
        properties = data["_properties"]
        keys_to_check = {
            "rollup",
            "formula",
            "last_edited_time",
            "created_time",
            "unique_id",
        }
        [
            properties.pop(key)
            for key, value in properties.items()
            if any(k in value for k in keys_to_check)
        ]
        return data

    def add_property(self, property_: PageProperty) -> None:
        self.properties.append(property_)
        setattr(self.properties, property_.name, property_)


def deserialize_page(data: dict[str, Any]) -> Page:
    return Page(**data)


__all__ = ["Page", "deserialize_page"]
