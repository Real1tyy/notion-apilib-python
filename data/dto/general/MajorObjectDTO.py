from typing import Optional, Annotated

from pydantic import AnyUrl

from ObjectDTO import ObjectDTO
from validators import icon_validator


class MajorObjectDTO(ObjectDTO):
    icon: Annotated[str, icon_validator]
    cover: Optional[str] = None
    url: AnyUrl
    public_url: Optional[AnyUrl] = None
