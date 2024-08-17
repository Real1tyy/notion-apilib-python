# First Party
from notion_apilib.data.structures import Parent

from ..data import Breadcrumb, ColumnList, Divider, Unsupported
from ._general import _create_block


def create_divider(parent: Parent) -> Divider:
    """
    Factory method to create Divider object
    :param parent: parent object
    :return: newly created Divider Object
    """
    return _create_block(
        Divider,
        parent=parent,
    )


def create_column_list(parent: Parent) -> ColumnList:
    """
    Factory method to create ColumnList object
    :param parent: parent object
    :return: newly created ColumnList Object
    """
    return _create_block(ColumnList, parent=parent)


def create_breadcrumb(parent: Parent) -> Breadcrumb:
    """
    Factory method to create Breadcrumb object
    :param parent: parent object
    :return: newly created Breadcrumb Object
    """
    return _create_block(Breadcrumb, parent=parent)


def create_unsupported(parent: Parent) -> Unsupported:
    """
    Factory method to create Unsupported object
    :param parent: parent object
    :return: newly created Unsupported Object
    """
    return _create_block(
        Unsupported,
        parent=parent,
    )


__all__ = [
    "create_divider",
    "create_column_list",
    "create_breadcrumb",
    "create_unsupported",
]
