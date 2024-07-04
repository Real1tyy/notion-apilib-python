from pydantic import BaseModel


class Object(BaseModel):
    object: str
    id: str

    created_time: str
    last_edited_time: str
    created_by: dict[str, str]
    last_edited_by: dict[str, str]

    # cover:
    # icon
    parent: dict[str, str]
    archived: bool

    url: str
    # public_url
    request_id: str

    class Config:
        orm_mode = True
