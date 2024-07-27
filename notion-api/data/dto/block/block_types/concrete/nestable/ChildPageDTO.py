from pydantic import UUID4

from BlockDTO import BlockDTO


class ChildPageDTO(BlockDTO):
    page_id: UUID4
