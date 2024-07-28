from typing import Callable, Any

from pydantic_core.core_schema import ValidationInfo


def catch_exceptions(func: Callable[[Any, ValidationInfo], Any]) -> Callable[[Any, ValidationInfo], Any]:
    def wrapper(v: Any, info: ValidationInfo) -> Any:
        try:
            return func(v, info)
        except KeyError as e:
            raise ValueError(f"Invalid format, did not find parameter: {e}")
        except Exception as e:
            raise ValueError(f"Invalid format, encountered an error: {e}")

    return wrapper
