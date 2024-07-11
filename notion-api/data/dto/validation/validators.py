from typing import Any

from pydantic_core.core_schema import ValidationInfo

from database.properties.DatabasePropertyFactory import DatabasePropertyFactory
from database.properties.PropertyDTO import PropertyDTO
from utils import catch_exceptions


@catch_exceptions
def parent_validator(v: dict[str, Any], info: ValidationInfo) -> str:
    parent_type: str = v["type"]
    if parent_type == "database_id":
        return v["database_id"]
    if parent_type == "page_id":
        return v["page_id"]
    if parent_type == "block_id":
        return v["block_id"]
    if parent_type == "workspace":
        return "workspace"
    raise ValueError("Invalid parent format, did not find the desired properties")


@catch_exceptions
def icon_validator(v: dict[str, Any], info: ValidationInfo) -> str:
    return v["external"]["url"]


@catch_exceptions
def attributes_validator(v: list[dict[str, Any]], info: ValidationInfo) -> str:
    if len(v) == 0:
        return ""
    return v[0]["plain_text"]


@catch_exceptions
def properties_validator(v: dict[str, Any], info: ValidationInfo) -> list[PropertyDTO]:
    properties = []

    for value in v.values():
        print(value)
        try:
            properties.append(DatabasePropertyFactory.create_concrete_property_dto(value))
        except Exception as e:
            print(value)
            raise e
    return properties
