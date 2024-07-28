from abc import ABC
from typing import Optional, Annotated

from pydantic import AnyUrl, BeforeValidator

from general.Object import Object
from validation.validators import icon_validator


class MajorObject(Object, ABC):
    icon: Annotated[str, BeforeValidator(icon_validator)]
    cover: Optional[str] = None
    url: Optional[AnyUrl] = None
    public_url: Optional[AnyUrl] = None
