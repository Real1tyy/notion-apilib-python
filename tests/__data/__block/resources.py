from typing import Literal

import pytest
from datetime import datetime, timezone

from notion_api.data.blocks import File, Image, Pdf, Video
from __data.block import add_block_data, assert_block_data_is_correct, create_block_structure
from __data.utils import create_rich_text_data, assert_rich_text_data
from functools import partial

# Constants
RESOURCE_URL = "https://example.com/resource"
FILE_URL = "https://example.com/file"
EXPIRY_TIME = "2022-03-01T19:05:00.000Z"
DATE_TIME_EXPIRY_TIME = datetime(2022, 3, 1, 19, 5, 0, tzinfo=timezone.utc)
CAPTION_CONTENT = "Sample Caption"
CAPTION_COLOR = "red"
FILE_NAME = "example_file.txt"
FILE_TYPE = "file"
EXTERNAL_TYPE = "external"


def _create_resources_attributes(block_type, file_type: Literal['file', 'external']) -> dict:
    @add_block_data(block_type)
    def resources_data():
        data = {
            "type": file_type,
        }
        if file_type == 'external':
            data["external"] = {
                "url": RESOURCE_URL,
            }
        else:
            data["file"] = {
                "url": FILE_URL,
                "expiry_time": EXPIRY_TIME,
            }
        return data

    return resources_data()


def _create_file_attributes(block_type, file_type: Literal['file', 'external']) -> dict:
    def file_data():
        resources_data = _create_resources_attributes(block_type, file_type)
        resources_data['file']["caption"] = [create_rich_text_data(CAPTION_CONTENT, CAPTION_COLOR)]
        resources_data['file']["name"] = FILE_NAME
        return resources_data

    return file_data()


@pytest.fixture(params=['file', 'external'])
def file_block(request):
    return partial(_create_file_attributes, file_type=request.param)


@pytest.fixture(params=['file', 'external'])
def resources_block(request):
    return partial(_create_resources_attributes, file_type=request.param)


@pytest.mark.parametrize("block_class", [Image, Pdf, Video])
def test_resources_structure(resources_block, block_class):
    item = create_block_structure(block_class, resources_block)
    assert_resources_data_correct(item)


def test_file_structure(file_block):
    item = create_block_structure(File, file_block)
    assert_file_data_correct(item)


def assert_file_data_correct(data: File):
    assert_resources_data_correct(data)
    file_data = data.file

    # Verify the caption
    assert len(file_data.caption) == 1
    assert_rich_text_data(file_data.caption[0], CAPTION_CONTENT, CAPTION_COLOR)
    assert file_data.name == FILE_NAME


def assert_resources_data_correct(data):
    block_type = data.__class__.get_associated_block_type()
    assert_block_data_is_correct(data, block_type)

    resources_data = getattr(data, f"{block_type.value}")
    if resources_data.type == EXTERNAL_TYPE:
        assert resources_data.external.url == RESOURCE_URL
    else:
        assert resources_data.type == FILE_TYPE
        assert resources_data.file.url == FILE_URL
        assert resources_data.file.expiry_time == DATE_TIME_EXPIRY_TIME
