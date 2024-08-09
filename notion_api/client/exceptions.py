from dataclasses import dataclass


@dataclass
class ResponseError(Exception):
    """
    Exception raised when a response from the Notion API indicates an error.

    Attributes:
        status_code (int): The HTTP status code from the response.
        message (str): The error message from the Notion API response.
    """
    status_code: int
    message: str
