from typing import Optional

from Page import Page
from PropertyType import PropertyType
from ResourcesAttributes import ResourcesAttributes
from ResourcesProperty import EmailPage, UrlPage, PhoneNumberPage, FilesPage
from factory.general import _create_page_property


def create_email_page(
        parent: Page, name: str, email: str, id_: Optional[str] = None) -> EmailPage:
    """
    Factory method to create an EmailPage object.

    Parameters:
        parent (Page): The parent page to which this email property belongs.
        name (str): The name of the email property.
        email (str): The email value of the property.
        id_ (Optional[str]): The optional ID of the email property.

    Returns:
        EmailPage: A new EmailPage object.
    """
    return _create_page_property(
        EmailPage,
        parent=parent,
        property_type=PropertyType.EMAIL,
        name=name,
        id_=id_,
        email=email
    )


def create_files_page(
        parent: Page, name: str, files: list[ResourcesAttributes], id_: Optional[str] = None) -> FilesPage:
    """
    Factory method to create a FilesPage object.

    Parameters:
        parent (Page): The parent page to which this files property belongs.
        name (str): The name of the files property.
        files (list[ResourcesAttributes]): The list of files for the property.
        id_ (Optional[str]): The optional ID of the files property.

    Returns:
        FilesPage: A new FilesPage object.
    """
    return _create_page_property(
        FilesPage,
        parent=parent,
        property_type=PropertyType.FILES,
        name=name,
        id_=id_,
        files=files
    )


def create_phone_number_page(
        parent: Page, name: str, phone_number: str, id_: Optional[str] = None) -> PhoneNumberPage:
    """
    Factory method to create a PhoneNumberPage object.

    Parameters:
        parent (Page): The parent page to which this phone number property belongs.
        name (str): The name of the phone number property.
        phone_number (str): The phone number value of the property.
        id_ (Optional[str]): The optional ID of the phone number property.

    Returns:
        PhoneNumberPage: A new PhoneNumberPage object.
    """
    return _create_page_property(
        PhoneNumberPage,
        parent=parent,
        property_type=PropertyType.PHONE_NUMBER,
        name=name,
        id_=id_,
        phone_number=phone_number
    )


def create_url_page(
        parent: Page, name: str, url: str, id_: Optional[str] = None) -> UrlPage:
    """
    Factory method to create a UrlPage object.

    Parameters:
        parent (Page): The parent page to which this URL property belongs.
        name (str): The name of the URL property.
        url (str): The URL value of the property.
        id_ (Optional[str]): The optional ID of the URL property.

    Returns:
        UrlPage: A new UrlPage object.
    """
    return _create_page_property(
        UrlPage,
        parent=parent,
        property_type=PropertyType.URL,
        name=name,
        id_=id_,
        url=url
    )
