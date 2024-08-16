# First Party
from notion_api.data._blocks._data.code import Code, CodeAttributes
from notion_api.data._blocks._factory.general import _create_block
from notion_api.data.structures import Parent, RichText


def create_code(parent: Parent, caption: list[RichText], rich_text: list[RichText], language: str) -> Code:
    """
    Factory method to create Code object
    :param parent: parent object
    :param caption: caption
    :param rich_text: rich text
    :param language: language
    :return: newly created Code Object
    """
    return _create_block(
        Code,
        parent=parent,
        block_type_specific_params=CodeAttributes(caption=caption, rich_text=rich_text, language=language)
    )


__all__ = [
    'create_code'
]
