# Third Party
from pydantic import BaseModel


class Annotations(BaseModel):
    bold: bool
    italic: bool
    strikethrough: bool
    underline: bool
    code: bool
    color: str


def create_basic_annotations_object() -> Annotations:
    return Annotations(bold=False, italic=False, strikethrough=False, underline=False, code=False, color='default')
