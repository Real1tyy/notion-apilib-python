import datetime
from typing import Any, Optional

from pydantic import BaseModel


class Object(BaseModel):
    id: str
    object: str

    created_time: datetime.datetime
    last_edited_time: datetime.datetime
    created_by: dict[str, Any]
    last_edited_by: dict[str, Any]

    cover: Optional[str]
    icon: dict[str, Any]
    parent: dict[str, Any]
    archived: bool
    in_trash: bool

    # properties: dict[str, Any]

    url: str
    public_url: Optional[str]
    request_id: str

    class Config:
        from_attributes = True
