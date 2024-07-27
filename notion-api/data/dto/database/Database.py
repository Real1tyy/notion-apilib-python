from typing import Annotated

from pydantic import BeforeValidator

from database.properties.Property import Property
from general.MajorObjectDTO import MajorObjectDTO
from validation.validators import attributes_validator, properties_validator


class Database(MajorObjectDTO):
    title: Annotated[str, BeforeValidator(attributes_validator)]
    description: Annotated[str, BeforeValidator(attributes_validator)]
    is_inline: bool
    properties: Annotated[list[Property], BeforeValidator(properties_validator)]
