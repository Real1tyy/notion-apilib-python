from uuid import UUID

from validators import catch_exceptions


@catch_exceptions
def related_database_validator(related_database_id: UUID) -> UUID:
    if related_database_id is None:
        raise ValueError("related_database_id cannot be None")
    return related_database_id
