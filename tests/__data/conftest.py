import pytest
from __data.constants import *
from __structures.conftest import parent_data, user_data, create_emoji, create_rich_text, text, mention, equation


@pytest.fixture
def object_data(parent_data, user_data):
    def return_object_data(object_type):
        return {
            "object": object_type,
            "id": OBJECT_ID,
            "parent": parent_data,
            "created_time": CREATED_TIME,
            "last_edited_time": LAST_EDITED_TIME,
            "created_by": user_data,
            "last_edited_by": user_data,
            "archived": False,
            "in_trash": False
        }

    return return_object_data


@pytest.fixture
def major_object_data(object_data):
    def return_major_object_data(object_type):
        data = object_data(object_type)
        major_data = {
            "cover": COVER,
            "icon": {
                "type": ICON_TYPE,
                "external": {
                    "url": ICON_URL
                }
            },
            "url": URL,
            "public_url": PUBLIC_URL,
        }
        data.update(major_data)
        return data

    return return_major_object_data
