import pytest
from datetime import datetime, timezone
from typing import Literal
from functools import partial

from notion_api.data.blocks import File, Image, Pdf, Video
from __block.helper import extract_create_assert_structure, extract_create_assert_serialization
from __block.assertions import assert_block_data_is_correct
from __structures.assertions import assert_rich_text_structure
from ..__structures.conftest import create_rich_text

# Constants
RESOURCE_URL = "https://example.com/resource"
FILE_URL = "https://example.com/file"
EXPIRY_TIME = datetime(2022, 3, 1, 19, 5, 0, tzinfo=timezone.utc)
DATE_TIME_EXPIRY_TIME = datetime(2022, 3, 1, 19, 5, 0, tzinfo=timezone.utc)
FILE_NAME = "example_file.txt"
FILE_TYPE = "file"
EXTERNAL_TYPE = "external"


@pytest.fixture(params=['file', 'external'])
def resources_block(request, block_data):
    def create_resources_attributes(block_type, file_type: Literal['file', 'external']) -> dict:
        resources_data = {
            "type": file_type,
        }
        if file_type == 'external':
            resources_data["external"] = {
                "url": RESOURCE_URL,
            }
        else:
            resources_data["file"] = {
                "url": FILE_URL,
                "expiry_time": EXPIRY_TIME,
            }
        return block_data(block_type, resources_data)

    return partial(create_resources_attributes, file_type=request.param)


@pytest.fixture()
def file_block(request, resources_block, create_rich_text):
    def create_file_attributes(block_type) -> dict:
        data = resources_block(block_type)
        data['file']['caption'] = create_rich_text
        data['file']['name'] = FILE_NAME
        return data

    return create_file_attributes


def assert_file_data_is_correct(data: File, expected_data: dict):
    assert_resources_data_is_correct(data, expected_data)
    file_data = data.file
    expected_file_data = expected_data["file"]

    assert_rich_text_structure(file_data.caption, expected_file_data["caption"])
    assert file_data.name == expected_file_data["name"]


def assert_resources_data_is_correct(data, expected_data: dict):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, expected_data)

    resources_data = getattr(data, f"{block_type.value}")
    expected_resources_data = expected_data[block_type.value]

    match resources_data.type:
        case "external":
            assert resources_data.external.url == expected_resources_data["external"]["url"]
        case "file":
            assert resources_data.file.url == expected_resources_data["file"]["url"]
            assert resources_data.file.expiry_time == expected_resources_data["file"]["expiry_time"]


@pytest.mark.parametrize("block_class", [Image, Pdf, Video])
def test_resources_structure(resources_block, block_class):
    extract_create_assert_structure(resources_block, block_class, assert_resources_data_is_correct)


@pytest.mark.parametrize("block_class", [Image, Pdf, Video])
def test_resources_serialization(resources_block, block_class):
    extract_create_assert_serialization(resources_block, block_class)


def test_file_structure(file_block):
    extract_create_assert_structure(file_block, File, assert_file_data_is_correct)


def test_file_serialization(file_block):
    extract_create_assert_serialization(file_block, File)
