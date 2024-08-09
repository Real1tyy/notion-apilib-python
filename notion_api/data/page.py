# Standard Library
from typing import Annotated, Any

from pydantic import BaseModel, BeforeValidator, Field
from pydantic_core.core_schema import ValidationInfo

# Third Party
from block import Block
from data.exceptions import catch_exceptions
from data.object import MajorObject
from data._properties.property import PageProperty
from data._properties.property_factory import deserialize_page_property


class PageProperties(BaseModel, extra="allow"):
    properties: list[PageProperty] = Field(exclude=True, default=[])


@catch_exceptions
def properties_validator(v: dict[str, Any], info: ValidationInfo) -> PageProperties:
    properties = []
    for key, value in v.items():
        value['name'] = key
        _class = deserialize_page_property(value)
        properties.append(_class)
        v[key] = _class

    v['_properties'] = properties
    return v


class Page(MajorObject):
    properties: Annotated[PageProperties, BeforeValidator(properties_validator)]
    children: list[Block] = Field(default=[])

    def get_properties(self) -> list[PageProperty]:
        return self.properties.properties

    def serialize_to_json(self) -> dict[str, Any]:
        data = self.model_dump(mode='json', exclude_none=True, exclude={'id', 'archived', 'children'})
        properties = data['_properties']
        keys_to_check = {'rollup', 'formula', 'last_edited_time', 'created_time', 'unique_id'}
        to_remove = [key for key, value in properties.items() if any(k in value for k in keys_to_check)]
        [properties.pop(key) for key in to_remove]
        return data

    def add_property(self, property_: PageProperty) -> list[PageProperty]:
        self.get_properties().append(property_)
        setattr(self.properties, property_.name, property_)
        return self.get_properties()


def create_page(data: dict[str, Any]) -> Page:
    return Page(**data)


__all__ = ["Page", "create_page", "PageProperties"]
