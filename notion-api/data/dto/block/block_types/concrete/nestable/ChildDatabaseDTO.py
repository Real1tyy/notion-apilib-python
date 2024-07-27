from pydantic import UUID4

from BlockDTO import BlockDTO


class ChildDatabaseDTO(BlockDTO):
    database_id: UUID4
