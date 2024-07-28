from typing import Optional

from pydantic import BaseModel

from Annotations import Annotations
from Equation import Equation
from Mention import Mention
from Text import Text


class RichText(BaseModel):
    type: str
    text: Text = None
    mention: Mention = None
    equation: Equation = None
    annotations: Annotations
    plain_text: str
    href: Optional[str]
