# Standard Library
import uuid
from datetime import datetime, timezone
from functools import wraps
from typing import Literal, Any, Callable, Dict

from notion_api.data.object import Object, MajorObject


def _create_object_data(object_type: Literal["block", "database", "page", "user", "workspace"]) -> dict[str, Any]:
    return {
        "object": object_type,
        "id": "c02fc1d3-db8b-45c5-a222-27595b15aea7",
        "parent": {
            "type": "page_id",
            "page_id": "59833787-2cf9-4fdf-8782-e53db20768a5"
        },
        "created_time": "2022-03-01T19:05:00.000Z",
        "last_edited_time": "2022-07-06T19:41:00.000Z",
        "created_by": {
            "object": "user",
            "id": "ee5f0f84-409a-440f-983a-a5315961c6e4"
        },
        "last_edited_by": {
            "object": "user",
            "id": "ee5f0f84-409a-440f-983a-a5315961c6e4"
        },
        "archived": False,
        "in_trash": False
    }


def _create_major_object_data(object_type: Literal["block", "database", "page", "user", "workspace"]) -> dict[str, Any]:
    data = _create_object_data(object_type)
    major_data = {
        "cover": None,
        "icon": {
            "type": "external",
            "external": {
                "url": "https://www.notion.so/icons/target_gray.svg"
            }
        },
        "url": "https://www.notion.so/1a91e289d5d9470d9e30ff1dfde63c60",
        "public_url": None,
    }
    data.update(major_data)
    return data


def add_object_data(object_type: Literal["block", "database", "page", "user", "workspace"]) -> Callable:
    """
    Decorator to add object-specific data to the dictionary returned by the decorated function.

    Args:
        object_type (Literal): The type of the object to be added.

    Returns:
        Callable: A decorated function that returns a dictionary extended with object data.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Dict[str, Any]:
            data = func(*args, **kwargs)
            object_data = _create_object_data(object_type)
            data.update(object_data)
            return data

        return wrapper

    return decorator


def add_major_object_data(object_type: Literal["block", "database", "page", "user", "workspace"]) -> Callable:
    """
    Decorator to add major object data (like cover, icon, and URL) to the dictionary returned by the decorated function.

    Args:
        object_type (Literal): The type of the object to be added.

    Returns:
        Callable: A decorated function that returns a dictionary extended with major object data.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Dict[str, Any]:
            data = func(*args, **kwargs)
            major_object_data = _create_major_object_data(object_type)
            data.update(major_object_data)
            return data

        return wrapper

    return decorator


def assert_object_data_is_correct(data: Object, expected_object_type: str):
    assert data.object == expected_object_type
    assert data.id == uuid.UUID("c02fc1d3db8b45c5a22227595b15aea7")
    assert data.created_time == datetime(2022, 3, 1, 19, 5, tzinfo=timezone.utc)
    assert data.last_edited_time == datetime(2022, 7, 6, 19, 41, tzinfo=timezone.utc)
    assert data.created_by.object == "user"
    assert data.created_by.id == uuid.UUID("ee5f0f84409a440f983aa5315961c6e4")
    assert data.last_edited_by.object == "user"
    assert data.last_edited_by.id == uuid.UUID("ee5f0f84409a440f983aa5315961c6e4")
    assert data.parent.type == "page_id"
    assert data.parent.page_id == uuid.UUID("598337872cf94fdf8782e53db20768a5")
    assert not data.archived
    assert not data.in_trash


def assert_major_object_data_is_correct(data: MajorObject, expected_object_type: str):
    assert_object_data_is_correct(data, expected_object_type)
    assert data.cover is None
    assert data.icon.type == "external"
    assert data.icon.external.url == "https://www.notion.so/icons/target_gray.svg"
    assert data.url == "https://www.notion.so/1a91e289d5d9470d9e30ff1dfde63c60"
    assert data.public_url is None
