# Standard Library
from typing import Annotated, Any

# Third Party
from pydantic import BeforeValidator, Field
from pydantic_core.core_schema import ValidationInfo

# First Party
from .exceptions_ import catch_exceptions
from .object_ import MajorObject
from .properties_structure import PropertiesStructure, parse_properties
from notion_api.data.properties import PageProperty, deserialize_page_property


@catch_exceptions
def properties_validator(
    v: dict[str, Any], info: ValidationInfo
) -> PropertiesStructure:
    return parse_properties(v, deserialize_page_property)


class Page(MajorObject):
    properties: Annotated[PropertiesStructure, BeforeValidator(properties_validator)]
    children: list["Block"] = Field(default=[])

    def get_properties(self) -> list[PageProperty]:
        return self.properties.properties

    def serialize_to_json(self) -> dict[str, Any]:
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

    def add_property(self, property_: PageProperty) -> list[PageProperty]:
        self.get_properties().append(property_)
        setattr(self.properties, property_.name, property_)
        return self.get_properties()


def deserialize_page(data: dict[str, Any]) -> Page:
    return Page(**data)


__all__ = ["Page", "deserialize_page"]
