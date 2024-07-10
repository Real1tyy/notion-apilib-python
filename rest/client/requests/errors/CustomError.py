from dataclasses import dataclass


@dataclass
class CustomError:
    status_code: int
    message: str
    # error_type: ErrorType
