from pydantic import BaseModel

from Block import Block


class LinkPreviewAttributes(BaseModel):
    url: str


class LinkPreview(Block):
    link_preview: LinkPreviewAttributes
