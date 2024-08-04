# Standard Library
from typing import Any

from pydantic import BaseModel, Field

# Third Party
from Property import DatabaseProperty, PageProperty


class CheckboxPage(PageProperty):
    """
    A model representing a checkbox property for a page.

    Attributes:
        checkbox (bool): The checkbox value of the page property.
    """
    checkbox: bool


class CheckboxDatabase(DatabaseProperty):
    """
    A model representing a checkbox property for a database.

    Attributes:
        checkbox (dict[str, Any]): The dictionary representing the checkbox property for the database.
    """
    checkbox: dict[str, Any]


class Option(BaseModel):
    """
    A model representing an option for multi-select and select properties.

    Attributes:
        id (str): The ID of the option.
        name (str): The name of the option.
        color (str): The color of the option.
    """
    id: str = Field(exclude=True)
    name: str
    color: str = Field(exclude=True)


class OptionStructure(BaseModel):
    """
    A model representing the structure for multi-select options.

    Attributes:
        options (list[Option]): A list of options for the multi-select property.
    """
    options: list[Option]


class MultiSelectPage(PageProperty):
    """
    A model representing a multi-select property for a page.

    Attributes:
        multi_select (OptionStructure): The multi-select structure of the page property.
    """
    multi_select: OptionStructure


class MultiSelectDatabase(DatabaseProperty):
    """
    A model representing a multi-select property for a database.

    Attributes:
        multi_select (OptionStructure): The multi-select structure of the database property.
    """
    multi_select: OptionStructure


class SelectPage(PageProperty):
    """
    A model representing a select property for a page.

    Attributes:
        select (Option): The select structure of the page property.
    """
    select: Option


class SelectDatabase(DatabaseProperty):
    """
    A model representing a select property for a database.

    Attributes:
        select (OptionStructure): The select structure of the database property.
    """
    select: OptionStructure


class Group(Option):
    """
    A model representing a group of options for status properties.

    Attributes:
        option_ids (list[str]): A list of option IDs in the group.
    """
    option_ids: list[str]


class StatusDatabaseStructure(BaseModel):
    """
    A model representing the structure for status properties in a database.

    Attributes:
        options (list[Option]): A list of options for the status property.
        groups (list[Group]): A list of groups for the status property.
    """
    options: list[Option] = Field(exclude=True)
    groups: list[Group] = Field(exclude=True)


class StatusPage(PageProperty):
    """
    A model representing a status property for a page.

    Attributes:
        status (Option): The status structure of the page property.
    """
    status: Option


class StatusDatabase(DatabaseProperty):
    """
    A model representing a status property for a database.

    Attributes:
        status (StatusDatabaseStructure): The status structure of the database property.
    """
    status: StatusDatabaseStructure
