# Standard Library
from typing import Optional

from data.Equation import Equation
from data.Mention import Mention
from pydantic import BaseModel

# Third Party
from Annotations import Annotations, create_basic_annotations_object
from Text import Text, create_text_object


class RichText(BaseModel):
    type: str
    text: Text = None
    mention: Mention = None
    equation: Equation = None
    annotations: Annotations
    plain_text: str
    href: Optional[str]

    def change_text(self, text: str):
        self.plain_text = text
        if self.text:
            self.text.content = text


def create_basic_rich_text_object(text: str) -> RichText:
    return RichText(
        type='text',
        text=create_text_object(text),
        annotations=create_basic_annotations_object(),
        plain_text=text,
        href=None
    )
