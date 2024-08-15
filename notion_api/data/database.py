# Standard Library
from typing import Annotated, Any

from pydantic import BeforeValidator, Field
from pydantic_core.core_schema import ValidationInfo

from notion_api.data.properties_structure import PropertiesStructure, parse_properties
from notion_api.data.structures import RichText
# Third Party
from notion_api.data.exceptions import catch_exceptions
from notion_api.data.object import MajorObject
from notion_api.data.page import Page
from notion_api.data.properties import DatabaseProperty, deserialize_database_property


@catch_exceptions
def properties_validator(v: dict[str, Any], info: ValidationInfo) -> PropertiesStructure:
    return parse_properties(v, deserialize_database_property)


class Database(MajorObject):
    title: list[RichText]
    description: list[RichText]
    is_inline: bool
    properties: Annotated[PropertiesStructure, BeforeValidator(properties_validator)]
    pages: list[Page] = Field(default=[], exclude=True)

    def get_properties(self) -> list[DatabaseProperty]:
        props = self.properties
        return props.properties

    def serialize_to_json(self) -> dict[str, Any]:
        data = self.model_dump(
            mode='json', exclude_none=True, exclude={'id', 'archived', 'last_edited_time', 'created_time'})
        properties = data['_properties']
        keys_to_check = {'rollup', 'formula', 'relation', 'unique_id'}
        [properties.pop(key) for key, value in properties.items() if any(k in value for k in keys_to_check)]
        return data

    def add_property(self, property_: DatabaseProperty) -> list[DatabaseProperty]:
        self.get_properties().append(property_)
        setattr(self.properties, property_.name, property_)
        return self.get_properties()


def deserialize_database(data: dict[str, Any]) -> Database:
    return Database(**data)


__all__ = ["Database", "deserialize_database"]
