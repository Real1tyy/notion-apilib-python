from pydantic import UUID4

from BlockDTO import BlockDTO


class MentionDTO(BlockDTO):
    type: str
    id: UUID4
