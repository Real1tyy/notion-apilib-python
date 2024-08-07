# Standard Library
from dataclasses import dataclass


@dataclass
class ApiError:
    status_code: int
    message: str
