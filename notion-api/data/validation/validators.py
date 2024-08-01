from typing import Any

from pydantic_core.core_schema import ValidationInfo

from database.properties.Property import Property
from database.properties.PropertyFactory import PropertyFactory
from validation.exceptions import catch_exceptions


@catch_exceptions
def attributes_validator(v: list[dict[str, Any]], info: ValidationInfo) -> str:
    if len(v) == 0:
        return ""
    return v[0]["plain_text"]


@catch_exceptions
def properties_validator(v: dict[str, Any], info: ValidationInfo) -> list[Property]:
    properties = []

    for value in v.values():
        properties.append(PropertyFactory.create_concrete_property_dto(value))
    return properties
