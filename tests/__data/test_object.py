from typing import Any

from tests.__data.assertions import assert_object_data_is_correct
from notion_api.data.object import MajorObject


class TestObject(MajorObject):

    def get_properties(self):
        # just for testing
        pass

    def add_property(self, property_):
        # just for testing
        pass

    def serialize_to_json(self) -> dict[str, Any]:
        return self.model_dump(mode='json', by_alias=True, exclude_none=True)


def test_extensively_object(extensive_major_object_data):
    object = TestObject(**extensive_major_object_data)
    assert_object_data_is_correct(object, extensive_major_object_data)
