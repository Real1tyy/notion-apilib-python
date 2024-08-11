from __data.constants import *
from notion_api.data.object import Object, MajorObject


def assert_object_data_is_correct(data: Object, expected_object_type: str):
    assert data.object == expected_object_type
    assert data.id == OBJECT_ID
    assert data.created_time == CREATED_TIME
    assert data.last_edited_time == LAST_EDITED_TIME
    assert data.created_by.object == "user"
    assert data.created_by.id == CREATED_BY_ID
    assert data.last_edited_by.object == "user"
    assert data.last_edited_by.id == LAST_EDITED_BY_ID
    assert data.parent.type == PARENT_TYPE
    assert data.parent.page_id == PARENT_PAGE_ID
    assert not data.archived
    assert not data.in_trash


def assert_major_object_data_is_correct(data: MajorObject, expected_object_type):
    assert_object_data_is_correct(data, expected_object_type)
    assert data.cover == COVER
    assert data.icon.type == ICON_TYPE
    assert data.icon.external.url == ICON_URL
    assert data.url == URL
    assert data.public_url is None
