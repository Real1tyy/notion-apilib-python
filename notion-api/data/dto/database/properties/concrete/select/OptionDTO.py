from typing import Optional

from pydantic import BaseModel

from OptionColor import OptionColor


class SelectOptionDTO(BaseModel):
    id: str
    name: str
    color: OptionColor
    description: Optional[str] = None
