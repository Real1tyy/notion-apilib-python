from ..__properties.assertion_assigner import get_assertion_function
from ..assertions import assert_major_object_data_is_correct


def assert_page_structure(page, expected_page):
    assert_major_object_data_is_correct(page, expected_page)
    for property_ in page.get_properties():
        assert property_.name in expected_page["properties"]
        assertion_func = get_assertion_function(property_.__class__)
        assertion_func(property_, expected_page["properties"][property_.name])
