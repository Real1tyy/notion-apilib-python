from typing import Optional

from pydantic import BaseModel

from Annotations import Annotations
from Text import Text


class RichText(BaseModel):
    type: str
    text: Text
    annotations: Annotations
    plain_text: str
    href: Optional[str]
