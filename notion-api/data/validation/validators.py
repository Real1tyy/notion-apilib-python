from typing import Any

from pydantic_core.core_schema import ValidationInfo

from PropertyTypeFactory import create_concrete_property_type
from database.properties.Property import Property
from validation.exceptions import catch_exceptions


@catch_exceptions
def properties_validator(v: dict[str, Any], info: ValidationInfo) -> list[Property]:
    properties = []

    for value in v.values():
        properties.append(create_concrete_property_type(value))
    return properties
