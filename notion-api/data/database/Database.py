from typing import Annotated

from pydantic import BeforeValidator

from Object import MajorObject
from Property import PageProperty
from RichText import RichText
from validation.validators import properties_validator


class Database(MajorObject):
    title: list[RichText]
    description: list[RichText]
    is_inline: bool
    properties: Annotated[list[PageProperty], BeforeValidator(properties_validator)]
