from .general import _create_page_property, _create_database_property
from notion_api.data._properties._data.option import (StatusPage, OptionPage, SelectPage, OptionStructurePage,
                                                      MultiSelectPage, \
                                                      CheckboxPage, \
                                                      CheckboxDatabase, MultiSelectDatabase, SelectDatabase, Group,
                                                      StatusDatabaseStructure, StatusDatabase)


def create_checkbox_page(
        parent: 'Page', name: str, checkbox: bool) -> CheckboxPage:
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
        name=name,
        property_specific_params=checkbox
    )


def create_checkbox_database(
        parent: 'Database', name: str) -> CheckboxDatabase:
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
        name=name,
        property_specific_params={}
    )


def create_multi_select_page(
        parent: 'Page', name: str, options: list[OptionPage]) -> MultiSelectPage:
    """
    Factory method to create a MultiSelectPage object.

    Parameters:
        parent (Page): The parent page to which this multi-select property belongs.
        name (str): The name of the multi-select property.
        options (list[OptionPage]): A list of options for the multi-select property.

    Returns:
        MultiSelectPage: A new MultiSelectPage object.
    """
    option_structure = OptionStructurePage(options=options)
    return _create_page_property(
        MultiSelectPage,
        parent=parent,
        name=name,
        property_specific_params=option_structure
    )


def create_multi_select_database(
        parent: 'Database', name: str, options: list[OptionPage]) -> MultiSelectDatabase:
    """
    Factory method to create a MultiSelectDatabase object.

    Parameters:
        parent (Database): The parent database to which this multi-select property belongs.
        name (str): The name of the multi-select property.
        options (list[OptionPage]): A list of options for the multi-select property.

    Returns:
        MultiSelectDatabase: A new MultiSelectDatabase object.
    """
    option_structure = OptionStructurePage(options=options)
    return _create_database_property(
        MultiSelectDatabase,
        parent=parent,
        name=name,
        property_specific_params=option_structure
    )


def create_select_page(
        parent: 'Page', name: str, option: OptionPage) -> SelectPage:
    """
    Factory method to create a SelectPage object.

    Parameters:
        parent (Page): The parent page to which this select property belongs.
        name (str): The name of the select property.
        option (OptionPage): The option for the select property.

    Returns:
        SelectPage: A new SelectPage object.
    """
    return _create_page_property(
        SelectPage,
        parent=parent,
        name=name,
        property_specific_params=option
    )


def create_select_database(
        parent: 'Database', name: str, options: list[OptionPage]) -> SelectDatabase:
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
        name=name,
        property_specific_params=OptionStructurePage(options=options)
    )


def create_status_page(
        parent: 'Page', name: str, status: OptionPage) -> StatusPage:
    """
    Factory method to create a StatusPage object.

    Parameters:
        parent (Page): The parent page to which this status property belongs.
        name (str): The name of the status property.
        status (OptionPage): The status option for the property.

    Returns:
        StatusPage: A new StatusPage object.
    """
    return _create_page_property(
        StatusPage,
        parent=parent,
        name=name,
        property_specific_params=status
    )


def create_status_database(
        parent: 'Database', name: str, options: list[OptionPage], groups: list[Group]) -> StatusDatabase:
    """
    Factory method to create a StatusDatabase object.

    Parameters:
        parent (Database): The parent database to which this status property belongs.
        name (str): The name of the status property.
        options (list[OptionPage]): A list of options for the status property.
        groups (list[Group]): A list of groups for the status property.

    Returns:
        StatusDatabase: A new StatusDatabase object.
    """
    status_structure = StatusDatabaseStructure(options=options, groups=groups)
    return _create_database_property(
        StatusDatabase,
        parent=parent,
        name=name,
        property_specific_params=status_structure
    )


__all__ = ['create_checkbox_page', 'create_checkbox_database', 'create_multi_select_page',
           'create_multi_select_database',
           'create_select_page', 'create_select_database', 'create_status_page', 'create_status_database']
