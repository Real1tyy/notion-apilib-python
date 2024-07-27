from pydantic import BaseModel


class Group(BaseModel):
    id: str
    name: str
    color: str
    option_ids: list[str]
