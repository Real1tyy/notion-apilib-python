# Third Party
from pydantic import BaseModel

from block.block import Block


class ChildAttributes(BaseModel):
    title: str


class ChildDatabase(Block):
    child_database: ChildAttributes


class ChildPage(Block):
    child_page: ChildAttributes
