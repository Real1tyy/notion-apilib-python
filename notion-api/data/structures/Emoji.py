from pydantic import BaseModel


class Emoji(BaseModel):
    emoji: str
    type: str
