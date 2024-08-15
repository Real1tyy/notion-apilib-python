# Third Party
from notion_api.data._properties.data import *
from notion_api.data._properties.type_ import PropertyType

PROPERTY_TYPE_MAP = {
    "checkbox": (CheckboxPage, CheckboxDatabase),
    "created_by": (CreatedByPage, CreatedByDatabase),
    "created_time": (CreatedTimePage, CreatedTimeDatabase),
    "date": (DatePage, DateDatabase),
    "email": (EmailPage, EmailDatabase),
    "files": (FilesPage, FilesDatabase),
    "formula": (FormulaPage, FormulaDatabase),
    "last_edited_by": (LastEditedByPage, LastEditedByDatabase),
    "last_edited_time": (LastEditedTimePage, LastEditedTimeDatabase),
    "multi_select": (MultiSelectPage, MultiSelectDatabase),
    "number": (NumberPage, NumberDatabase),
    "people": (PeoplePage, PeopleDatabase),
    "phone_number": (PhoneNumberPage, PhoneNumberDatabase),
    "relation": (RelationPage, RelationDatabase),
    "rollup": (RollupPage, RollupDatabase),
    "status": (StatusPage, StatusDatabase),
    "unique_id": (UniqueIdPage, UniqueIdDatabase),
    "url": (UrlPage, UrlDatabase),
    "select": (SelectPage, SelectDatabase),
    "title": (TitlePage, TitleDatabase),
    "rich_text": (RichTextPage, RichTextDatabase)
}


def deserialize_page_property(data: dict):
    """
    Create an instance of a concrete page property type based on the given data.

    Parameters
    ----------
    data : dict
        The data used to create the page property, including the property type.

    Returns
    -------
    PageProperty
        An instance of the concrete page property type.
    """
    property_type = PropertyType(data["type"])
    return PROPERTY_TYPE_MAP[property_type][0](**data)


def deserialize_database_property(data: dict):
    """
    Create an instance of a concrete database property type based on the given data.

    Parameters
    ----------
    data : dict
        The data used to create the database property, including the property type.

    Returns
    -------
    DatabaseProperty
        An instance of the concrete database property type.
    """
    property_type = PropertyType(data["type"])
    return PROPERTY_TYPE_MAP[property_type][1](**data)


__all__ = [
    'deserialize_page_property', 'deserialize_database_property']
