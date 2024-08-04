from typing import Optional

from Page import Page
from PropertyType import PropertyType
from SelectProperty import StatusPage, Option, SelectPage, OptionStructure, MultiSelectPage, CheckboxPage
from factory.general import _create_page_property


def create_checkbox_page(
        parent: Page, name: str, checkbox: bool, id_: Optional[str] = None) -> CheckboxPage:
    """
    Factory method to create a CheckboxPage object.

    Parameters:
        parent (Page): The parent page to which this checkbox property belongs.
        name (str): The name of the checkbox property.
        checkbox (bool): The checkbox value of the property.
        id_ (Optional[str]): The optional ID of the checkbox property.

    Returns:
        CheckboxPage: A new CheckboxPage object.
    """
    return _create_page_property(
        CheckboxPage,
        parent=parent,
        property_type=PropertyType.CHECKBOX,
        name=name,
        id_=id_,
        checkbox=checkbox
    )


def create_multi_select_page(
        parent: Page, name: str, options: list[Option], id_: Optional[str] = None) -> MultiSelectPage:
    """
    Factory method to create a MultiSelectPage object.

    Parameters:
        parent (Page): The parent page to which this multi-select property belongs.
        name (str): The name of the multi-select property.
        options (list[Option]): A list of options for the multi-select property.
        id_ (Optional[str]): The optional ID of the multi-select property.

    Returns:
        MultiSelectPage: A new MultiSelectPage object.
    """
    option_structure = OptionStructure(options=options)
    return _create_page_property(
        MultiSelectPage,
        parent=parent,
        property_type=PropertyType.MULTI_SELECT,
        name=name,
        id_=id_,
        multi_select=option_structure
    )


def create_select_page(
        parent: Page, name: str, option: Option, id_: Optional[str] = None) -> SelectPage:
    """
    Factory method to create a SelectPage object.

    Parameters:
        parent (Page): The parent page to which this select property belongs.
        name (str): The name of the select property.
        option (Option): The option for the select property.
        id_ (Optional[str]): The optional ID of the select property.

    Returns:
        SelectPage: A new SelectPage object.
    """
    return _create_page_property(
        SelectPage,
        parent=parent,
        property_type=PropertyType.SELECT,
        name=name,
        id_=id_,
        select=option
    )


def create_status_page(
        parent: Page, name: str, status: Option, id_: Optional[str] = None) -> StatusPage:
    """
    Factory method to create a StatusPage object.

    Parameters:
        parent (Page): The parent page to which this status property belongs.
        name (str): The name of the status property.
        status (Option): The status option for the property.
        id_ (Optional[str]): The optional ID of the status property.

    Returns:
        StatusPage: A new StatusPage object.
    """
    return _create_page_property(
        StatusPage,
        parent=parent,
        property_type=PropertyType.STATUS,
        name=name,
        id_=id_,
        status=status
    )
