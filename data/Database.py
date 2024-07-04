# from Page import Page
# from PropertyTypes import PropertyTypes
from main.data.Object import Object


class Database(Object):

    class Config:
        orm_mode = True
