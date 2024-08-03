from typing import Any, Annotated

from pydantic import BeforeValidator, BaseModel, Field
from pydantic_core.core_schema import ValidationInfo

from Object import MajorObject
from Property import PageProperty
from PropertyTypeFactory import create_concrete_page_property_type
from custom_types import json_
from exceptions import catch_exceptions


class PageProperties(BaseModel, extra="allow"):
    properties: list[PageProperty] = Field(exclude=True, default=[])


@catch_exceptions
def properties_validator(v: dict[str, Any], info: ValidationInfo) -> PageProperties:
    properties = []
    for key, value in v.items():
        value['name'] = key
        _class = create_concrete_page_property_type(value)
        properties.append(_class)
        v[key] = _class

    v['properties'] = properties
    return v


class Page(MajorObject):
    properties: Annotated[PageProperties, BeforeValidator(properties_validator)]

    def get_properties(self) -> list[PageProperty]:
        return self.properties.properties

    def deserialize_json(self) -> json_:
        data = self.model_dump(mode='json', exclude_none=True, exclude={'id', 'archived'})
        properties = data['properties']
        keys_to_check = {'rollup', 'formula', 'last_edited_time', 'created_time', 'unique_id'}
        to_remove = [key for key, value in properties.items() if any(k in value for k in keys_to_check)]
        [properties.pop(key) for key in to_remove]
        return data


def create_page(data: json_) -> Page:
    return Page(**data)
