import pytest
from tests.__data.constants import *
from tests.__data.__structures.conftest import (create_parent_data, create_user_data, create_emoji, create_rich_text,
                                                create_text, \
                                                create_mention, create_equation, create_resource, create_external,
                                                create_file_object, create_extensive_parent_data,
                                                create_extensive_user_data,
                                                create_href, create_extensive_resource)


@pytest.fixture(params=OBJECT_TYPES)
def extensive_object_data(request, create_extensive_parent_data, create_extensive_user_data):
    return {
        "object": request.param,
        "id": OBJECT_ID,
        "parent": create_extensive_parent_data,
        "created_time": CREATED_TIME,
        "last_edited_time": LAST_EDITED_TIME,
        "created_by": create_extensive_user_data,
        "last_edited_by": create_extensive_user_data,
        "archived": False,
        "in_trash": False
    }


@pytest.fixture
def object_data(create_parent_data, create_user_data):
    def return_object_data(object_type):
        return {
            "object": object_type,
            "id": OBJECT_ID,
            "parent": create_parent_data,
            "created_time": CREATED_TIME,
            "last_edited_time": LAST_EDITED_TIME,
            "created_by": create_user_data,
            "last_edited_by": create_user_data,
            "archived": False,
            "in_trash": False
        }

    return return_object_data


@pytest.fixture
def major_object_data(object_data, create_resource):
    def return_major_object_data(object_type):
        data = object_data(object_type)
        major_data = {
            "cover": COVER,
            "icon": create_resource,
            "url": URL,
            "public_url": PUBLIC_URL,
        }
        data.update(major_data)
        return data

    return return_major_object_data


@pytest.fixture
def extensive_major_object_data(extensive_object_data, create_extensive_resource):
    extensive_object_data = extensive_object_data.copy()
    major_data = {
        "cover": COVER,
        "icon": create_extensive_resource,
        "url": URL,
        "public_url": PUBLIC_URL,
    }
    extensive_object_data.update(major_data)
    return extensive_object_data
