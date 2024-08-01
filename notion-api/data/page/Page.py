from typing import Any

from pydantic_core.core_schema import ValidationInfo

from Object import MajorObject
from Property import Property
from exceptions import catch_exceptions


@catch_exceptions
def properties_validator(v: dict[str, Any], info: ValidationInfo) -> list[Property]:
    return v


class Page(MajorObject):
    pass
    # properties: Annotated[list[Property], BeforeValidator(properties_validator)]
