from Property import PageProperty, DatabaseProperty
from RichText import RichText


class RichTextPage(PageProperty):
    rich_text: list[RichText]


class RichTextDatabase(DatabaseProperty):
    pass


class TitlePage(PageProperty):
    title: list[RichText]


class TitleDatabase(DatabaseProperty):
    pass
