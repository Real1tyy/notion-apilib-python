# First Party
from notion_api.data.object_ import MajorObject, Object
from tests.__data.__structures.assertions import (
    assert_icon_structure,
    assert_parent_structure,
    assert_user_structure,
)


def assert_object_data_is_correct(data: Object, expected_data: dict):
    assert data.object == expected_data["object"]
    assert data.id == expected_data["id"]
    assert data.created_time == expected_data["created_time"]
    assert data.last_edited_time == expected_data["last_edited_time"]
    assert_user_structure(data.created_by, expected_data["created_by"])
    assert_user_structure(data.last_edited_by, expected_data["last_edited_by"])
    assert_parent_structure(data.parent, expected_data["parent"])
    assert not data.archived
    assert not data.in_trash


def assert_major_object_data_is_correct(data: MajorObject, expected_data: dict):
    assert_object_data_is_correct(data, expected_data)
    assert_icon_structure(data.icon, expected_data["icon"])
    assert data.cover == expected_data["cover"]
    assert data.url == expected_data["url"]
    assert data.public_url is None
