from pydantic import UUID4

from Block import Block


class ChildDatabase(Block):
    database_id: UUID4
