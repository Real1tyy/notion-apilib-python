from pydantic import UUID4

from Block import Block


class Mention(Block):
    type: str
    id: UUID4
