# Standard Library
from typing import Any

# Third Party
from _properties.property import DatabaseProperty, PageProperty
from structures import ResourcesAttributes


class EmailPage(PageProperty):
    """
    A model representing an email property for a page.

    Attributes:
        email (str): The email value of the page property.
    """
    email: str


class EmailDatabase(DatabaseProperty):
    """
    A model representing an email property for a database.

    Attributes:
        email (dict[str, Any]): The dictionary representing the email property for the database.
    """
    email: dict[str, Any]


class FilesPage(PageProperty):
    """
    A model representing a files property for a page.

    Attributes:
        files (list[ResourcesAttributes]): The list of files for the page property.
    """
    files: list[ResourcesAttributes]


class FilesDatabase(DatabaseProperty):
    """
    A model representing a files property for a database.

    Attributes:
        files (dict[str, Any]): The dictionary representing the files property for the database.
    """
    files: dict[str, Any]


class PhoneNumberPage(PageProperty):
    """
    A model representing a phone number property for a page.

    Attributes:
        phone_number (str): The phone number value of the page property.
    """
    phone_number: str


class PhoneNumberDatabase(DatabaseProperty):
    """
    A model representing a phone number property for a database.

    Attributes:
        phone_number (dict[str, Any]): The dictionary representing the phone number property for the database.
    """
    phone_number: dict[str, Any]


class UrlPage(PageProperty):
    """
    A model representing a URL property for a page.

    Attributes:
        url (str): The URL value of the page property.
    """
    url: str


class UrlDatabase(DatabaseProperty):
    """
    A model representing a URL property for a database.

    Attributes:
        url (dict[str, Any]): The dictionary representing the URL property for the database.
    """
    url: dict[str, Any]
