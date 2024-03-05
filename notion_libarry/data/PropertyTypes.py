from enum import Enum


class PropertyTypes(Enum):
    TEXT = 1
    NUMBER = 2
    SELECT = 3
    MULTI_SELECT = 4
    STATUS = 5
    DATE = 6
    PERSON = 7
    FILES_MEDIA = 8
    CHECKBOX = 9
    URL = 10
    EMAIL = 11
    PHONE = 12
    FORMULA = 13
    RELATION = 14
    ROLLUP = 15
    CREATED_TIME = 16
    CREATED_BY = 17
    LAST_EDITED_TIME = 18
    LAST_EDITED_BY = 19
    BUTTON = 20
    ID = 21
