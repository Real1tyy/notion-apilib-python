# Standard Library
from typing import Any

# First Party
from notion_apilib.data.object_ import MajorObject
from tests.__data.assertions import assert_object_data_is_correct


class ObjectForTesting(MajorObject):

    def properties(self):
        # just for testing
        pass

    def add_property(self, property_):
        # just for testing
        pass

    def serialize_to_json(self) -> dict[str, Any]:
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)


def test_extensively_object(extensive_major_object_data):
    object_ = ObjectForTesting(**extensive_major_object_data)
    assert_object_data_is_correct(object_, extensive_major_object_data)
