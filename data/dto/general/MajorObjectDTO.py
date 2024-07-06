from typing import Optional, Annotated

from pydantic import AnyUrl, BeforeValidator

from general.ObjectDTO import ObjectDTO
from validators import icon_validator


class MajorObjectDTO(ObjectDTO):
    icon: Annotated[str, BeforeValidator(icon_validator)]
    cover: Optional[str] = None
    url: AnyUrl
    public_url: Optional[AnyUrl] = None
