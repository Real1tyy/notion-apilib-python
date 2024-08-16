# Standard Library
import json
from abc import ABC

# Third Party
from pydantic import BaseModel


class BasicConfiguration(BaseModel, ABC, use_enum_values=True, from_attributes=True, arbitrary_types_allowed=True):
    """
    Abstract model class used for basic pydantic configuration to be reused by other classes
    """

    def to_json_string(self) -> str:
        """
        returns json string utilizing model_dump method and indents it for readability used for debugging and
        printing out purposes
        :return:
        """
        return json.dumps(self.model_dump(mode='json', by_alias=True, exclude_none=True), indent=4)


class ExtraConfiguration(BasicConfiguration, ABC, extra='allow'):
    """
    Represents an abstract model class that extends BasicConfiguration class with the addition of allowing extra
    fields to be passed in
    """
    pass
