from _data.ResourcesAttributes import ResourcesAttributes
from _properties.type_ import PropertyType
from database import Database
from general import _create_page_property, _create_database_property
from page import Page
from resources import EmailPage, UrlPage, PhoneNumberPage, FilesPage, EmailDatabase, FilesDatabase, \
    PhoneNumberDatabase, UrlDatabase


def create_email_page(
        parent: Page, name: str, email: str) -> EmailPage:
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
        property_type=PropertyType.EMAIL,
        name=name,
        email=email
    )


def create_email_database(
        parent: Database, name: str) -> EmailDatabase:
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
        property_type=PropertyType.EMAIL,
        name=name,
        email={}
    )


def create_files_page(
        parent: Page, name: str, files: list[ResourcesAttributes]) -> FilesPage:
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
        property_type=PropertyType.FILES,
        name=name,
        files=files
    )


def create_files_database(
        parent: Database, name: str) -> FilesDatabase:
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
        property_type=PropertyType.FILES,
        name=name,
        files={}
    )


def create_phone_number_page(
        parent: Page, name: str, phone_number: str) -> PhoneNumberPage:
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
        property_type=PropertyType.PHONE_NUMBER,
        name=name,
        phone_number=phone_number
    )


def create_phone_number_database(
        parent: Database, name: str) -> PhoneNumberDatabase:
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
        property_type=PropertyType.PHONE_NUMBER,
        name=name,
        phone_number={}
    )


def create_url_page(
        parent: Page, name: str, url: str) -> UrlPage:
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
        property_type=PropertyType.URL,
        name=name,
        url=url
    )


def create_url_database(
        parent: Database, name: str) -> UrlDatabase:
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
        property_type=PropertyType.URL,
        name=name,
        url={}
    )
