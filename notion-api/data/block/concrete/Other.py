from Block import Block, _create_block_object
from BlockType import BlockType
from Parent import Parent


class Divider(Block):
    pass


def create_divider_object(parent: Parent) -> Divider:
    """
    Factory method to create Divider object
    :param parent: parent object
    :return: newly created Divider Object
    """
    return _create_block_object(
        Divider,
        parent=parent,
        block_type=BlockType.DIVIDER,
    )


class ColumnList(Block):
    pass


def create_column_list_object(parent: Parent) -> ColumnList:
    """
    Factory method to create ColumnList object
    :param parent: parent object
    :return: newly created ColumnList Object
    """
    return _create_block_object(
        ColumnList,
        parent=parent,
        block_type=BlockType.COLUMN_LIST,
    )


class Breadcrumb(Block):
    pass


def create_breadcrumb_object(parent: Parent) -> Breadcrumb:
    """
    Factory method to create Breadcrumb object
    :param parent: parent object
    :return: newly created Breadcrumb Object
    """
    return _create_block_object(
        Breadcrumb,
        parent=parent,
        block_type=BlockType.BREADCRUMB,
    )


class Unsupported(Block):
    pass


def create_unsupported_object(parent: Parent) -> Unsupported:
    """
    Factory method to create Unsupported object
    :param parent: parent object
    :return: newly created Unsupported Object
    """
    return _create_block_object(
        Unsupported,
        parent=parent,
        block_type=BlockType.UNSUPPORTED,
    )
