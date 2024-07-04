from main.data.Object import Object
from main.data.PageProperties import PageProperties


class Page(Object):
    properties: PageProperties

    class Config:
        orm_mode = True
