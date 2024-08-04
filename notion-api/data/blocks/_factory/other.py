from Parent import Parent

from block import _create_block
from data.other import Divider, ColumnList, Breadcrumb, Unsupported
from type import BlockType


def create_divider(parent: Parent) -> Divider:
    """
    Factory method to create Divider object
    :param parent: parent object
    :return: newly created Divider Object
    """
    return _create_block(
        Divider,
        parent=parent,
        block_type=BlockType.DIVIDER,
    )


def create_column_list(parent: Parent) -> ColumnList:
    """
    Factory method to create ColumnList object
    :param parent: parent object
    :return: newly created ColumnList Object
    """
    return _create_block(
        ColumnList,
        parent=parent,
        block_type=BlockType.COLUMN_LIST,
    )


def create_breadcrumb(parent: Parent) -> Breadcrumb:
    """
    Factory method to create Breadcrumb object
    :param parent: parent object
    :return: newly created Breadcrumb Object
    """
    return _create_block(
        Breadcrumb,
        parent=parent,
        block_type=BlockType.BREADCRUMB,
    )


def create_unsupported(parent: Parent) -> Unsupported:
    """
    Factory method to create Unsupported object
    :param parent: parent object
    :return: newly created Unsupported Object
    """
    return _create_block(
        Unsupported,
        parent=parent,
        block_type=BlockType.UNSUPPORTED,
    )
