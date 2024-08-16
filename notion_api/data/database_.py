# Standard Library
from typing import Annotated, Any

# Third Party
from pydantic import BeforeValidator, Field, field_validator
from pydantic_core.core_schema import ValidationInfo

# First Party
from .object_ import MajorObject
from .page_ import Page
from .properties_structure import PropertiesStructure, parse_properties
from notion_api.data.properties import DatabaseProperty, deserialize_database_property
from notion_api.data.structures import RichText


class Database(MajorObject):
    title: list[RichText]
    description: list[RichText]
    is_inline: bool
    properties_attributes: PropertiesStructure[DatabaseProperty] = Field(alias="properties")
    pages: list[Page] = Field(default=[], exclude=True)

    @field_validator("properties_attributes", mode="before")
    @classmethod
    def validate_properties(cls, v: Any) -> PropertiesStructure:
        return parse_properties(v, deserialize_database_property)

    @property
    def properties(self) -> list[DatabaseProperty]:
        return self.properties_attributes.properties

    def serialize_to_json(self) -> dict[str, Any]:
        data = self.model_dump(
            mode="json",
            exclude_none=True,
            exclude={"id", "archived", "last_edited_time", "created_time"},
        )
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


def deserialize_database(data: dict[str, Any]) -> Database:
    return Database(**data)


__all__ = ["Database", "deserialize_database"]
