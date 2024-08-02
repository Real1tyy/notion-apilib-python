from typing import Any

from pydantic_core.core_schema import ValidationInfo

from Property import PageProperty
from PropertyTypeFactory import create_concrete_page_property_type
from validation.exceptions import catch_exceptions


@catch_exceptions
def properties_validator(v: dict[str, Any], info: ValidationInfo) -> list[PageProperty]:
    properties = []

    for value in v.values():
        properties.append(create_concrete_page_property_type(value))
    return properties
