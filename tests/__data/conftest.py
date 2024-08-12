import pytest

import pytest
from __data.constants import *


@pytest.fixture
def object_data():
    def return_object_data(object_type):
        return {
            "object": object_type,
            "id": OBJECT_ID,
            "parent": {
                "type": PARENT_TYPE,
                "page_id": PARENT_PAGE_ID
            },
            "created_time": CREATED_TIME,
            "last_edited_time": LAST_EDITED_TIME,
            "created_by": {
                "object": "user",
                "id": CREATED_BY_ID
            },
            "last_edited_by": {
                "object": "user",
                "id": LAST_EDITED_BY_ID
            },
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
