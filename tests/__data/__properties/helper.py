from typing import Type, Callable

from notion_api.data.properties import Property
from .assertions import extract_property_data, create_property_object, assert_serialization_to_json


def extract_create_assert_structure(data_provider, property_class: Type[Property], assert_structure_func: Callable):
    data = extract_property_data(data_provider, property_class)
    property_ = create_property_object(data, property_class)
    assert_structure_func(property_, data)


def extract_create_assert_serialization(data_provider, property_class: Type[Property]):
    data = extract_property_data(data_provider, property_class)
    property_ = create_property_object(data, property_class)
    assert_serialization_to_json(property_, data[property_class.get_payload_property_name()])
