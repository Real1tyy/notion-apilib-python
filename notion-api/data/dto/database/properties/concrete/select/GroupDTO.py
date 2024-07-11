from pydantic import BaseModel

from OptionColor import OptionColor


class GroupDTO(BaseModel):
    id: str
    name: str
    color: OptionColor
    option_ids: list[str]
