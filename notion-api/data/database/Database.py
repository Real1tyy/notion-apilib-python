from typing import Annotated

from pydantic import BeforeValidator

from Object import MajorObject
from RichText import RichText
from database.properties.Property import Property
from validation.validators import properties_validator


class Database(MajorObject):
    title: list[RichText]
    description: list[RichText]
    is_inline: bool
    properties: Annotated[list[Property], BeforeValidator(properties_validator)]
