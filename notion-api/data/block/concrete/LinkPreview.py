from pydantic import BaseModel

from Block import Block, _create_block_object
from BlockType import BlockType
from Parent import Parent


class LinkPreviewAttributes(BaseModel):
    url: str


class LinkPreview(Block):
    link_preview: LinkPreviewAttributes


def create_link_preview_object(parent: Parent, url: str) -> LinkPreview:
    """
    Factory method to create LinkPreview object
    :param parent: parent object
    :param url: URL for the link preview
    :return: newly created LinkPreview Object
    """
    return _create_block_object(
        LinkPreview,
        parent=parent,
        block_type=BlockType.LINK_PREVIEW,
        link_preview=LinkPreviewAttributes(url=url)
    )
