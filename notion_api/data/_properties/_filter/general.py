from pydantic import BaseModel


class FilterStructure(BaseModel, extra='allow'):
    """
    Represents the inner filter structure used in notion database query api.
    """
    pass
