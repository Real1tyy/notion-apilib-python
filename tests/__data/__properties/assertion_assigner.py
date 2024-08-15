from notion_api.data.properties import (
    DatePage, DateDatabase, FormulaPage, FormulaDatabase, NumberPage, NumberDatabase,
    UniqueIdPage, UniqueIdDatabase, CheckboxPage, CheckboxDatabase, MultiSelectPage,
    MultiSelectDatabase, SelectPage, SelectDatabase, StatusPage, StatusDatabase,
    RelationPage, RelationDatabase, RollupPage, RollupDatabase, EmailPage, EmailDatabase,
    FilesPage, FilesDatabase, PhoneNumberPage, PhoneNumberDatabase, RichTextPage, RichTextDatabase,
    TitlePage, TitleDatabase, UrlPage, UrlDatabase, CreatedTimePage, CreatedTimeDatabase,
    LastEditedTimePage, LastEditedTimeDatabase, CreatedByPage, CreatedByDatabase,
    LastEditedByPage, LastEditedByDatabase, PeoplePage, PeopleDatabase
)
from .test_date import assert_date_page_is_correct, assert_date_database_is_correct
from .test_formula import assert_formula_page_is_correct, assert_formula_database_is_correct
from .test_number import (assert_number_page_is_correct, assert_number_database_is_correct,
                          assert_unique_id_page_is_correct, assert_unique_id_database_is_correct)
from .test_option import assert_checkbox_page_is_correct, assert_checkbox_database_is_correct, \
    assert_multi_select_page_is_correct, assert_multi_select_database_is_correct, assert_select_page_is_correct, \
    assert_select_database_is_correct, assert_status_database_is_correct, assert_status_page_is_correct
from .test_relation import assert_relation_page_is_correct, assert_relation_database_is_correct, \
    assert_rollup_page_is_correct, assert_rollup_database_is_correct
from .test_resource import (assert_email_page_is_correct, assert_email_database_is_correct,
                            assert_files_page_is_correct, \
                            assert_files_database_is_correct, assert_phone_number_page_is_correct,
                            assert_phone_number_database_is_correct,
                            assert_url_database_is_correct, assert_url_page_is_correct)
from .test_text import assert_rich_text_page_is_correct, assert_rich_text_database_is_correct, \
    assert_title_page_is_correct, \
    assert_title_database_is_correct
from .test_time import (assert_created_time_page_is_correct, assert_created_time_database_is_correct,
                        assert_last_edited_time_page_is_correct,
                        assert_last_edited_time_database_is_correct)
from .test_user import (assert_created_by_page_is_correct, assert_created_by_database_is_correct,
                        assert_last_edited_by_page_is_correct, assert_last_edited_by_database_is_correct,
                        assert_people_page_is_correct, assert_people_database_is_correct)

ASSERTIONS_MAP = {
    DatePage: assert_date_page_is_correct,
    DateDatabase: assert_date_database_is_correct,
    FormulaPage: assert_formula_page_is_correct,
    FormulaDatabase: assert_formula_database_is_correct,
    NumberPage: assert_number_page_is_correct,
    NumberDatabase: assert_number_database_is_correct,
    UniqueIdPage: assert_unique_id_page_is_correct,
    UniqueIdDatabase: assert_unique_id_database_is_correct,
    CheckboxPage: assert_checkbox_page_is_correct,
    CheckboxDatabase: assert_checkbox_database_is_correct,
    MultiSelectPage: assert_multi_select_page_is_correct,
    MultiSelectDatabase: assert_multi_select_database_is_correct,
    SelectPage: assert_select_page_is_correct,
    SelectDatabase: assert_select_database_is_correct,
    StatusPage: assert_status_page_is_correct,
    StatusDatabase: assert_status_database_is_correct,
    RelationPage: assert_relation_page_is_correct,
    RelationDatabase: assert_relation_database_is_correct,
    RollupPage: assert_rollup_page_is_correct,
    RollupDatabase: assert_rollup_database_is_correct,
    EmailPage: assert_email_page_is_correct,
    EmailDatabase: assert_email_database_is_correct,
    FilesPage: assert_files_page_is_correct,
    FilesDatabase: assert_files_database_is_correct,
    PhoneNumberPage: assert_phone_number_page_is_correct,
    PhoneNumberDatabase: assert_phone_number_database_is_correct,
    RichTextPage: assert_rich_text_page_is_correct,
    RichTextDatabase: assert_rich_text_database_is_correct,
    TitlePage: assert_title_page_is_correct,
    TitleDatabase: assert_title_database_is_correct,
    UrlPage: assert_url_page_is_correct,
    UrlDatabase: assert_url_database_is_correct,
    CreatedTimePage: assert_created_time_page_is_correct,
    CreatedTimeDatabase: assert_created_time_database_is_correct,
    LastEditedTimePage: assert_last_edited_time_page_is_correct,
    LastEditedTimeDatabase: assert_last_edited_time_database_is_correct,
    CreatedByPage: assert_created_by_page_is_correct,
    CreatedByDatabase: assert_created_by_database_is_correct,
    LastEditedByPage: assert_last_edited_by_page_is_correct,
    LastEditedByDatabase: assert_last_edited_by_database_is_correct,
    PeoplePage: assert_people_page_is_correct,
    PeopleDatabase: assert_people_database_is_correct,
}


def get_assertion_function(property_class):
    """
    Retrieve the assertion function for a given property class.

    Parameters:
        property_class (type): The class of the property.

    Returns:
        function: The corresponding assertion function.
    """
    return ASSERTIONS_MAP.get(property_class)
