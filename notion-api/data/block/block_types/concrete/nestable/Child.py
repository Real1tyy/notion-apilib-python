from pydantic import BaseModel

from Block import Block


class ChildAttributes(BaseModel):
    title: str


class ChildDatabase(Block):
    child_database: ChildAttributes


class ChildPage(Block):
    child_page: ChildAttributes
