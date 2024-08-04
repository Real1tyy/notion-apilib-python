# Standard Library
from functools import wraps
from typing import Any, Callable

# Third Party
from ApiError import ApiError
from returns.result import Failure, Result, Success
from status_codes import ERROR


def handle_return(result: Any) -> Result[ApiError, Any]:
    if isinstance(result, Failure):
        return result
    return Success(result)


def handle_exceptions(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Result[ApiError, Any]:
        try:
            result = func(*args, **kwargs)
            return handle_return(result)
        except Exception as e:
            return Failure(ApiError(message=str(e), status_code=ERROR))

    return wrapper
