from typing import Any, Annotated

from pydantic import BeforeValidator, BaseModel
from pydantic_core.core_schema import ValidationInfo

from Object import MajorObject
from PropertyTypeFactory import create_concrete_page_property_type
from exceptions import catch_exceptions


class PageProperties(BaseModel, extra="allow"):
    pass


@catch_exceptions
def properties_validator(v: dict[str, Any], info: ValidationInfo) -> PageProperties:
    for key, value in v.items():
        _class = create_concrete_page_property_type(value)
        v[key] = _class

    return v


class Page(MajorObject):
    properties: Annotated[PageProperties, BeforeValidator(properties_validator)]
