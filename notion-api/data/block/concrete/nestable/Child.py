from pydantic import BaseModel

from Block import Block, _create_block
from BlockType import BlockType
from Parent import Parent


class ChildAttributes(BaseModel):
    title: str


class ChildDatabase(Block):
    child_database: ChildAttributes


def create_child_database(
        parent: Parent,
        title: str,
        children: list['Block'] = None
) -> ChildDatabase:
    """
    Factory method to create ChildDatabase object
    :param parent: parent object
    :param title: title of the child database
    :param children: optional list of child blocks
    :return: newly created ChildDatabase Object
    """
    return _create_block(
        ChildDatabase,
        parent=parent,
        block_type=BlockType.CHILD_DATABASE,
        children=children,
        child_database=ChildAttributes(title=title)
    )


class ChildPage(Block):
    child_page: ChildAttributes


def create_child_page(
        parent: Parent,
        title: str,
        children: list['Block'] = None
) -> ChildPage:
    """
    Factory method to create ChildPage object
    :param parent: parent object
    :param title: title of the child page
    :param children: optional list of child blocks
    :return: newly created ChildPage Object
    """
    return _create_block(
        ChildPage,
        parent=parent,
        block_type=BlockType.CHILD_PAGE,
        children=children,
        child_page=ChildAttributes(title=title)
    )
