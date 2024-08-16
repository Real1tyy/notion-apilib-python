# Standard Library
from typing import Any
from uuid import UUID

# Third Party
from pydantic import BaseModel, Field

# First Party
from ..property import DatabaseProperty, PageProperty
from ..type_ import PropertyType


class CheckboxPage(PageProperty):
    """
    A model representing a checkbox property for a page.

    Attributes:
        checkbox (bool): The checkbox value of the page property.
    """

    checkbox: bool

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.CHECKBOX


class CheckboxDatabase(DatabaseProperty):
    """
    A model representing a checkbox property for a database.

    Attributes:
        checkbox (dict[str, Any]): The dictionary representing the checkbox property for the database.
    """

    checkbox: dict[str, Any]

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.CHECKBOX


class OptionPage(BaseModel):
    """
    A model representing an option for multi-select and select _properties.

    Attributes:
        id (str): The ID of the option.
        name (str): The name of the option.
        color (str): The color of the option.
    """

    id: UUID = Field(exclude=True)
    name: str
    color: str = Field(exclude=True)


class OptionDatabase(BaseModel):
    """
    A model representing an option for multi-select and select _properties.

    Attributes:
        id (str): The ID of the option.
        name (str): The name of the option.
        color (str): The color of the option.
    """

    id: UUID = Field(exclude=True)
    name: str
    color: str


class OptionStructurePage(BaseModel):
    """
    A model representing the structure for multi-select options.

    Attributes:
        options (list[OptionPage]): A list of options for the multi-select property.
    """

    options: list[OptionPage]


class OptionStructureDatabase(BaseModel):
    """
    A model representing the structure for multi-select options.

    Attributes:
        options (list[OptionPage]): A list of options for the multi-select property.
    """

    options: list[OptionDatabase]


class MultiSelectPage(PageProperty):
    """
    A model representing a multi-select property for a page.

    Attributes:
        multi_select (OptionStructurePage): The multi-select structure of the page property.
    """

    multi_select: OptionStructurePage

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.MULTI_SELECT


class MultiSelectDatabase(DatabaseProperty):
    """
    A model representing a multi-select property for a database.

    Attributes:
        multi_select (OptionStructurePage): The multi-select structure of the database property.
    """

    multi_select: OptionStructureDatabase

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.MULTI_SELECT


class SelectPage(PageProperty):
    """
    A model representing a select property for a page.

    Attributes:
        select (OptionPage): The select structure of the page property.
    """

    select: OptionPage

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.SELECT


class SelectDatabase(DatabaseProperty):
    """
    A model representing a select property for a database.

    Attributes:
        select (OptionStructurePage): The select structure of the database property.
    """

    select: OptionStructureDatabase

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.SELECT


class Group(OptionDatabase):
    """
    A model representing a group of options for status _properties.

    Attributes:
        option_ids (list[str]): A list of option IDs in the group.
    """

    option_ids: list[UUID]


class StatusDatabaseStructure(BaseModel):
    """
    A model representing the structure for status _properties in a database.

    Attributes:
        options (list[OptionPage]): A list of options for the status property.
        groups (list[Group]): A list of groups for the status property.
    """

    options: list[OptionDatabase]
    groups: list[Group]


class StatusPage(PageProperty):
    """
    A model representing a status property for a page.

    Attributes:
        status (OptionPage): The status structure of the page property.
    """

    status: OptionPage

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.STATUS


class StatusDatabase(DatabaseProperty):
    """
    A model representing a status property for a database.

    Attributes:
        status (StatusDatabaseStructure): The status structure of the database property.
    """

    status: StatusDatabaseStructure

    @classmethod
    def get_associated_property_type(cls) -> PropertyType:
        return PropertyType.STATUS


__all__ = [
    "CheckboxPage",
    "CheckboxDatabase",
    "MultiSelectPage",
    "MultiSelectDatabase",
    "SelectPage",
    "SelectDatabase",
    "StatusPage",
    "StatusDatabase",
]
