from .assertions import assert_rich_text_value
from notion_api.data.structures import RichText


def test_rich_text_structure(create_extensive_rich_text):
    print()
    print(create_extensive_rich_text)
    rich_text = RichText(**(create_extensive_rich_text[0]))
    assert_rich_text_value(rich_text, create_extensive_rich_text[0])