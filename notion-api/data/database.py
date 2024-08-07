# Standard Library
from typing import Annotated, Any

from pydantic import BaseModel, BeforeValidator, Field
from pydantic_core.core_schema import ValidationInfo

from structures import RichText
# Third Party
from data.exceptions import catch_exceptions
from data.object import MajorObject
from data.page import Page
from data._properties.property import DatabaseProperty
from data._properties.property_factory import create_concrete_database_property_type


class DatabaseProperties(BaseModel, extra="allow"):
    properties: list[DatabaseProperty] = Field(exclude=True, default=[])


@catch_exceptions
def properties_validator(v: dict[str, Any], info: ValidationInfo) -> DatabaseProperties:
    properties = []
    for key, value in v.items():
        value['name'] = key
        _class = create_concrete_database_property_type(value)
        properties.append(_class)
        v[key] = _class

    v['_properties'] = properties
    return v


class Database(MajorObject):
    title: list[RichText]
    description: list[RichText]
    is_inline: bool
    properties: Annotated[DatabaseProperties, BeforeValidator(properties_validator)]
    pages: list[Page] = Field(default=[], exclude=True)

    def get_properties(self) -> list[DatabaseProperty]:
        return self.properties.properties

    def serialize_to_json(self) -> dict[str, Any]:
        data = self.model_dump(
            mode='json', exclude_none=True, exclude={'id', 'archived', 'in_trash',
                                                     'last_edited_time', 'created_time'})
        properties = data['_properties']
        keys_to_check = {'rollup', 'formula', 'relation', 'unique_id'}
        to_remove = [key for key, value in properties.items() if any(k in value for k in keys_to_check)]
        [properties.pop(key) for key in to_remove]
        return data

    def add_property(self, property_: DatabaseProperty) -> list[DatabaseProperty]:
        self.get_properties().append(property_)
        setattr(self.properties, property_.name, property_)
        return self.get_properties()


def create_database(data: dict[str, Any]) -> Database:
    return Database(**data)
