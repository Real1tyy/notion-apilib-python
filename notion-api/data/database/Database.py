from typing import Annotated

from pydantic import BeforeValidator

from Object import MajorObject
from database.properties.Property import Property
from validation.validators import attributes_validator, properties_validator


class Database(MajorObject):
    title: Annotated[str, BeforeValidator(attributes_validator)]
    description: Annotated[str, BeforeValidator(attributes_validator)]
    is_inline: bool
    properties: Annotated[list[Property], BeforeValidator(properties_validator)]
