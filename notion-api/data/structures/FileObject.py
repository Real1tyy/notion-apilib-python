from datetime import datetime

from pydantic import BaseModel
from pydantic_core import Url


class FileObject(BaseModel):
    url: Url
    expiry_time: datetime


class External(BaseModel):
    url: Url
