from pydantic import UUID4

from Block import Block


class ChildPage(Block):
    page_id: UUID4
