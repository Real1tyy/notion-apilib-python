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


class UrlPageProperty(PageProperty):
    pass


class PhoneNumberPageProperty(PageProperty):
    pass
