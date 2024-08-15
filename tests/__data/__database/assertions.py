from ..assertions import assert_major_object_data_is_correct
from ..__properties.assertion_assigner import get_assertion_function


def assert_database_structure(database, expected_database):
    assert_major_object_data_is_correct(database, expected_database)
    assert database.title == expected_database["title"]
    assert database.description == expected_database["description"]
    assert database.is_inline == expected_database["is_inline"]

    for property_ in database.get_properties():
        assert property_.name in expected_database["properties"]
        assertion_func = get_assertion_function(property_.__class__)
        assertion_func(property_, expected_database["properties"][property_.name])
