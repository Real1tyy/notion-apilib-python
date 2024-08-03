from typing import Any

from Property import PageProperty, DatabaseProperty
from ResourcesAttributes import ResourcesAttributes


class EmailPage(PageProperty):
    email: str


class EmailDatabase(DatabaseProperty):
    email: dict[str, Any]


class FilesPage(PageProperty):
    files: list[ResourcesAttributes]


class FilesDatabase(DatabaseProperty):
    files: dict[str, Any]


class PhoneNumberPage(PageProperty):
    phone_number: str


class PhoneNumberDatabase(DatabaseProperty):
    phone_number: dict[str, Any]


class UrlPage(PageProperty):
    url: str


class UrlDatabase(DatabaseProperty):
    url: dict[str, Any]
