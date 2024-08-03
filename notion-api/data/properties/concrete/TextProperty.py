from Property import PageProperty, DatabaseProperty
from RichText import RichText


class RichTextPage(PageProperty):
    rich_text: list[RichText]

    def change_text(self, text: str):
        if len(self.rich_text) > 0:
            self.rich_text[0].change_text(text)


class RichTextDatabase(DatabaseProperty):
    pass


class TitlePage(PageProperty):
    title: list[RichText]


class TitleDatabase(DatabaseProperty):
    pass
