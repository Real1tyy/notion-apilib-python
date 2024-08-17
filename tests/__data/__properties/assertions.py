# Standard Library
from typing import Callable, Type, TypeVar

# First Party
from notion_apilib.data.properties import Property
from tests.__data.utils.__serialization import transform_dictionary


def assert_properties_data_is_correct(data: Property, expected_data: dict):
    assert data.id == expected_data["id"]
    assert data.type == expected_data["type"]
    assert data.name == expected_data["name"]


T = TypeVar("T", bound=Property)


def extract_property_data(data_provider: Callable, property_class: Type[T]) -> dict:
    property_type = property_class.get_associated_property_type()
    return data_provider(property_type)


def create_property_object(property_data: dict, property_class: Type[T]) -> T:
    property_ = property_class(**property_data)
    assert property_.__class__ == property_class
    return property_


def assert_serialization_to_json(property_, property_type_specific_data):
    property_data = transform_dictionary(property_type_specific_data)
    json = property_.serialize_to_json()
    property_name = property_.__class__.get_payload_property_name()
    if property_type_specific_data != {}:
        assert json[property_name] == property_data
