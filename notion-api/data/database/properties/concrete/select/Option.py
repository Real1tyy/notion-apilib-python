from typing import Optional

from pydantic import BaseModel


class Option(BaseModel):
    id: str
    name: str
    color: str
    description: Optional[str] = None
