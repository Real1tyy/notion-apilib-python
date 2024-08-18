# First Party
from tests.__data.__structures.assertions import assert_rich_text_structure

from ..__properties.assertion_assigner import get_assertion_function
from ..assertions import assert_major_object_data_is_correct


def assert_database_structure(database, expected_database):
    assert_major_object_data_is_correct(database, expected_database)
    assert_rich_text_structure(database.title_structure, expected_database["title"])
    assert_rich_text_structure(
        database.description_structure, expected_database["description"]
    )
    assert database.is_inline == expected_database["is_inline"]

    for property_ in database.properties:
        assert property_.name in expected_database["properties"]
        assertion_func = get_assertion_function(property_.__class__)
        assertion_func(property_, expected_database["properties"][property_.name])
