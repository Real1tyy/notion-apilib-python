from Property import PageProperty, DatabaseProperty
from ResourcesAttributes import ResourcesAttributes


class EmailPage(PageProperty):
    email: str


class EmailDatabase(DatabaseProperty):
    pass


class FilesPage(PageProperty):
    files: list[ResourcesAttributes]


class FilesDatabase(DatabaseProperty):
    pass


class PhoneNumberPage(PageProperty):
    phone_number: str


class PhoneNumberDatabase(DatabaseProperty):
    pass


class UrlPage(PageProperty):
    url: str


class UrlDatabase(DatabaseProperty):
    pass
