from structures import ResourcesAttributes
from .general import _create_page_property, _create_database_property
from notion_api.data._properties.data import (EmailPage, UrlPage, PhoneNumberPage, FilesPage, EmailDatabase,
                                              FilesDatabase, \
                                              PhoneNumberDatabase, UrlDatabase)


def create_email_page(
        parent: 'Page', name: str, email: str) -> EmailPage:
    """
    Factory method to create an EmailPage object.

    Parameters:
        parent (Page): The parent page to which this email property belongs.
        name (str): The name of the email property.
        email (str): The email value of the property.

    Returns:
        EmailPage: A new EmailPage object.
    """
    return _create_page_property(
        EmailPage,
        parent=parent,
        name=name,
        property_specific_params=email
    )


def create_email_database(
        parent: 'Database', name: str) -> EmailDatabase:
    """
    Factory method to create an EmailDatabase object.

    Parameters:
        parent (Database): The parent database to which this email property belongs.
        name (str): The name of the email property.

    Returns:
        EmailDatabase: A new EmailDatabase object.
    """
    return _create_database_property(
        EmailDatabase,
        parent=parent,
        name=name,
        property_specific_params={}
    )


def create_files_page(
        parent: 'Page', name: str, files: list[ResourcesAttributes]) -> FilesPage:
    """
    Factory method to create a FilesPage object.

    Parameters:
        parent (Page): The parent page to which this files property belongs.
        name (str): The name of the files property.
        files (list[ResourcesAttributes]): The list of files for the property.

    Returns:
        FilesPage: A new FilesPage object.
    """
    return _create_page_property(
        FilesPage,
        parent=parent,
        name=name,
        property_specific_params=files
    )


def create_files_database(
        parent: 'Database', name: str) -> FilesDatabase:
    """
    Factory method to create a FilesDatabase object.

    Parameters:
        parent (Database): The parent database to which this files property belongs.
        name (str): The name of the files property.

    Returns:
        FilesDatabase: A new FilesDatabase object.
    """
    return _create_database_property(
        FilesDatabase,
        parent=parent,
        name=name,
        property_specific_params={}
    )


def create_phone_number_page(
        parent: 'Page', name: str, phone_number: str) -> PhoneNumberPage:
    """
    Factory method to create a PhoneNumberPage object.

    Parameters:
        parent (Page): The parent page to which this phone number property belongs.
        name (str): The name of the phone number property.
        phone_number (str): The phone number value of the property.

    Returns:
        PhoneNumberPage: A new PhoneNumberPage object.
    """
    return _create_page_property(
        PhoneNumberPage,
        parent=parent,
        name=name,
        property_specific_params=phone_number
    )


def create_phone_number_database(
        parent: 'Database', name: str) -> PhoneNumberDatabase:
    """
    Factory method to create a PhoneNumberDatabase object.

    Parameters:
        parent (Database): The parent database to which this phone number property belongs.
        name (str): The name of the phone number property.

    Returns:
        PhoneNumberDatabase: A new PhoneNumberDatabase object.
    """
    return _create_database_property(
        PhoneNumberDatabase,
        parent=parent,
        name=name,
        property_specific_params={}
    )


def create_url_page(
        parent: 'Page', name: str, url: str) -> UrlPage:
    """
    Factory method to create a UrlPage object.

    Parameters:
        parent (Page): The parent page to which this URL property belongs.
        name (str): The name of the URL property.
        url (str): The URL value of the property.

    Returns:
        UrlPage: A new UrlPage object.
    """
    return _create_page_property(
        UrlPage,
        parent=parent,
        name=name,
        property_specific_params=url
    )


def create_url_database(
        parent: 'Database', name: str) -> UrlDatabase:
    """
    Factory method to create a UrlDatabase object.

    Parameters:
        parent (Database): The parent database to which this URL property belongs.
        name (str): The name of the URL property.

    Returns:
        UrlDatabase: A new UrlDatabase object.
    """
    return _create_database_property(
        UrlDatabase,
        parent=parent,
        name=name,
        property_specific_params={}
    )


__all__ = ['create_email_page', 'create_email_database', 'create_files_page', 'create_files_database',
           'create_phone_number_page', 'create_phone_number_database', 'create_url_page', 'create_url_database']
