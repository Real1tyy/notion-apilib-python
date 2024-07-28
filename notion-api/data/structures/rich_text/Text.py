from typing import Optional

from pydantic import BaseModel


class Text(BaseModel):
    content: str
    link: Optional[str]
