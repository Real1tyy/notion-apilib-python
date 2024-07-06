from typing import Any, Callable

from pydantic_core.core_schema import ValidationInfo


def catch_exceptions(func: Callable[[Any, ValidationInfo], Any]) -> Callable[[Any, ValidationInfo], Any]:
    def wrapper(v: Any, info: ValidationInfo) -> Any:
        try:
            return func(v, info)
        except KeyError as e:
            raise ValueError(f"Invalid format, did not find parameter: {e}")
        except Exception as e:
            raise ValueError(f"Invalid format, encountered an error: {e}")

    return wrapper


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
    return v[0]["plain_text"]


@catch_exceptions
def properties_validator(v: dict[str, Any], info: ValidationInfo) -> Any:
    for key, value in v.items():
