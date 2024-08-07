from _properties.type_ import PropertyType
from data.database import Database
from _properties._factory.general import _create_page_property, _create_database_property
from data.page import Page
from _properties.data import StatusPage, Option, SelectPage, OptionStructure, MultiSelectPage, CheckboxPage, \
    CheckboxDatabase, MultiSelectDatabase, SelectDatabase, Group, StatusDatabaseStructure, StatusDatabase


def create_checkbox_page(
        parent: Page, name: str, checkbox: bool) -> CheckboxPage:
    """
    Factory method to create a CheckboxPage object.

    Parameters:
        parent (Page): The parent page to which this checkbox property belongs.
        name (str): The name of the checkbox property.
        checkbox (bool): The checkbox value of the property.

    Returns:
        CheckboxPage: A new CheckboxPage object.
    """
    return _create_page_property(
        CheckboxPage,
        parent=parent,
        property_type=PropertyType.CHECKBOX,
        name=name,
        checkbox=checkbox
    )


def create_checkbox_database(
        parent: Database, name: str) -> CheckboxDatabase:
    """
    Factory method to create a CheckboxDatabase object.

    Parameters:
        parent (Database): The parent database to which this checkbox property belongs.
        name (str): The name of the checkbox property.

    Returns:
        CheckboxDatabase: A new CheckboxDatabase object.
    """
    return _create_database_property(
        CheckboxDatabase,
        parent=parent,
        property_type=PropertyType.CHECKBOX,
        name=name,
        checkbox={}
    )


def create_multi_select_page(
        parent: Page, name: str, options: list[Option]) -> MultiSelectPage:
    """
    Factory method to create a MultiSelectPage object.

    Parameters:
        parent (Page): The parent page to which this multi-select property belongs.
        name (str): The name of the multi-select property.
        options (list[Option]): A list of options for the multi-select property.

    Returns:
        MultiSelectPage: A new MultiSelectPage object.
    """
    option_structure = OptionStructure(options=options)
    return _create_page_property(
        MultiSelectPage,
        parent=parent,
        property_type=PropertyType.MULTI_SELECT,
        name=name,
        multi_select=option_structure
    )


def create_multi_select_database(
        parent: Database, name: str, options: list[Option]) -> MultiSelectDatabase:
    """
    Factory method to create a MultiSelectDatabase object.

    Parameters:
        parent (Database): The parent database to which this multi-select property belongs.
        name (str): The name of the multi-select property.
        options (list[Option]): A list of options for the multi-select property.

    Returns:
        MultiSelectDatabase: A new MultiSelectDatabase object.
    """
    option_structure = OptionStructure(options=options)
    return _create_database_property(
        MultiSelectDatabase,
        parent=parent,
        property_type=PropertyType.MULTI_SELECT,
        name=name,
        multi_select=option_structure
    )


def create_select_page(
        parent: Page, name: str, option: Option) -> SelectPage:
    """
    Factory method to create a SelectPage object.

    Parameters:
        parent (Page): The parent page to which this select property belongs.
        name (str): The name of the select property.
        option (Option): The option for the select property.

    Returns:
        SelectPage: A new SelectPage object.
    """
    return _create_page_property(
        SelectPage,
        parent=parent,
        property_type=PropertyType.SELECT,
        name=name,
        select=option
    )


def create_select_database(
        parent: Database, name: str, options: list[Option]) -> SelectDatabase:
    """
    Factory method to create a SelectDatabase object.

    Parameters:
        parent (Database): The parent database to which this select property belongs.
        name (str): The name of the select property.
        options (list(Option)): The options for the select property.

    Returns:
        SelectDatabase: A new SelectDatabase object.
    """
    return _create_database_property(
        SelectDatabase,
        parent=parent,
        property_type=PropertyType.SELECT,
        name=name,
        select=OptionStructure(options=options)
    )


def create_status_page(
        parent: Page, name: str, status: Option) -> StatusPage:
    """
    Factory method to create a StatusPage object.

    Parameters:
        parent (Page): The parent page to which this status property belongs.
        name (str): The name of the status property.
        status (Option): The status option for the property.

    Returns:
        StatusPage: A new StatusPage object.
    """
    return _create_page_property(
        StatusPage,
        parent=parent,
        property_type=PropertyType.STATUS,
        name=name,
        status=status
    )


def create_status_database(
        parent: Database, name: str, options: list[Option], groups: list[Group]) -> StatusDatabase:
    """
    Factory method to create a StatusDatabase object.

    Parameters:
        parent (Database): The parent database to which this status property belongs.
        name (str): The name of the status property.
        options (list[Option]): A list of options for the status property.
        groups (list[Group]): A list of groups for the status property.

    Returns:
        StatusDatabase: A new StatusDatabase object.
    """
    status_structure = StatusDatabaseStructure(options=options, groups=groups)
    return _create_database_property(
        StatusDatabase,
        parent=parent,
        property_type=PropertyType.STATUS,
        name=name,
        status=status_structure
    )
